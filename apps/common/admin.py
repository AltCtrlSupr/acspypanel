from django.contrib import admin
from .models import ACSPermission
from ..domain.models import Domain
from ..maildomain.models import MailDomain
from django.contrib.contenttypes.models import ContentType

def remove_from_fieldsets(fieldsets, fields):
    for fieldset in fieldsets:
        for field in fields:
            if field in fieldset[1]['fields']:
                new_fields = []
                for new_field in fieldset[1]['fields']:
                    if not new_field in fields:
                        new_fields.append(new_field)

                fieldset[1]['fields'] = tuple(new_fields)
                break

    return fieldsets

def remove_from_list_display(list_display, fields):
    for field in fields:
        if field in list_display:
            list_display.remove(field)

    return list_display

class ACSModelAdmin(admin.ModelAdmin):
#    list_editable = [ 'enabled' ]
    def save_model(self, request, obj, form, change):
        super(ACSModelAdmin, self).save_model(request, obj, form, change)
        obj.save()
        self.add_users_to_model(request, obj, change)

    def save_formset(self, request, form, formset, change):
        super(ACSModelAdmin, self).save_formset(request, form, formset, change)
        formset.save()
        for f in formset.forms:
            self.add_users_to_model(request, f.instance, change)

    def add_users_to_model(self, request, obj, change):
        if not obj.pk: return False
        obj.save()
        (perm, created) = ACSPermission.objects.get_or_create(content_type=ContentType.objects.get_for_model(obj), object_id=obj.pk)

        parents_fk = [ 'domain', 'hosting', 'database', 'dns_domain', 'parent_domain', 'resource' , 'owner', 'httpd_host', 'rcpt' ]
        for fk in parents_fk:
            if hasattr(obj, fk):
                fk_obj = getattr(obj, fk, None)
                if not isinstance(fk_obj, unicode) and fk_obj is not None and hasattr(fk_obj, 'permission'):
                    for p in fk_obj.permission.all():
                        for u in p.user.all():
                            perm.user.add(u)


        if hasattr(obj, 'adminuser'):
            perm.user.add(obj.adminuser)
        perm.user.add(request.user.pk)
        perm.save()

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(ACSModelAdmin, self).get_fieldsets(request, obj)
        if not request.user.is_superuser:
            fieldsets = remove_from_fieldsets(fieldsets, ['user'])
        return fieldsets

    def get_list_display(self, request):
        list_display = super(ACSModelAdmin, self).get_list_display(request)
        if not request.user.is_superuser:
            list_display = remove_from_list_display(list_display, ['user'])
        return list_display

    def get_queryset(self, request):
        qs = super(ACSModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class ACSPermissionAdmin(admin.ModelAdmin):
    list_filter = [ 'content_type' ]
    list_display = [ 'content_type', 'content_object', 'get_users' ]

admin.site.register(ACSPermission, ACSPermissionAdmin)
