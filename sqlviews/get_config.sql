CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `get_config` AS
    select 
        `Service`.`name` AS `Service`,
        `ConfigItem`.`key` AS `ConfigKey`,
        `ConfigValue`.`value` AS `ConfigValue`
    from
        ((`config_configvalue` `ConfigValue`
        join `config_service` `Service` ON ((`ConfigValue`.`service_id` = `Service`.`id`)))
        join `config_configitem` `ConfigItem` ON ((`ConfigValue`.`setting_key_id` = `ConfigItem`.`id`)))
