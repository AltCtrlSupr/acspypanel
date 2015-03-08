-- Assuming default port 80 for listening, TODO change this
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `web_root` AS
    select 
        concat(`Server`.`home_base`,
                '/',
                `Hosting`.`name`,
                '/web/',
                `Domain`.`domain`) AS `DocumentRoot`,
        if(isnull(`HTTP`.`configuration`),
            '',
            `HTTP`.`configuration`) AS `Configuration`,
        `HTTP`.`php` AS `PHPEnabled`,
        (`Server`.`uid_base` + `Hosting`.`owner_id`) AS `UID`,
        (`Server`.`gid_base` + `Hosting`.`id`) AS `GID`,
        `IP`.`ip` AS `ListenIP`,
        `Service`.`name` AS `Service`
    from
        (((((`httphost_httphost` `HTTP`
        join `domain_domain` `Domain` ON ((`HTTP`.`domain_id` = `Domain`.`id`)))
        join `hosting_hosting` `Hosting` ON ((`Domain`.`hosting_id` = `Hosting`.`id`)))
        join `config_service` `Service` ON ((`HTTP`.`service_id` = `Service`.`id`)))
        join `config_server` `Server` ON ((`Service`.`server_id` = `Server`.`id`)))
        join `config_ipaddress` `IP` ON ((`Service`.`ip_id` = `IP`.`id`)))
