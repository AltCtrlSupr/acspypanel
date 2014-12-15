from django.contrib import admin

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
    def save_model(self, request, obj, form, change):
        if hasattr(obj, 'user_id'):
            if not obj.user_id:
                obj.user_id = request.user.id
        obj.save()

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
