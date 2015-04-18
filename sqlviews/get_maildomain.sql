CREATE VIEW `get_maildomain` AS
    select 
        `Domain`.`domain` AS `domain`,
        `Maildomain`.`backupmx` AS `backupmx`,
        `Service`.`name` AS `service`
    from
        (((`maildomain_maildomain` `Maildomain`
        join `domain_domain` `Domain` ON ((`Maildomain`.`domain_id` = `Domain`.`id`)))
        join `config_service` `Service` ON ((`Maildomain`.`service_id` = `Service`.`id`)))
        join `config_server` `Server` ON ((`Service`.`server_id` = `Server`.`id`)))
