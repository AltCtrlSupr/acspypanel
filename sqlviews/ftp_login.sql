CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `ftp_login` AS
    select 
        `User`.`username` AS `User`,
        `Account`.`password` AS `Password`,
        concat(`Server`.`home_base`,
                '/',
                `Hosting`.`name`,
                `FTP`.`dir`) AS `Homedir`,
        (`Server`.`uid_base` + `Account`.`id`) AS `UID`,
        (`Server`.`gid_base` + `Hosting`.`id`) AS `GID`,
        `Service`.`name` AS `Service`
    from
        ((((((`ftpd_ftpduser` `FTP`
        join `account_account` `Account` ON ((`FTP`.`username_id` = `Account`.`id`)))
        join `auth_user` `User` ON ((`Account`.`adminuser_id` = `User`.`id`)))
        join `domain_domain` `Domain` ON ((`Account`.`domain_id` = `Domain`.`id`)))
        join `hosting_hosting` `Hosting` ON ((`Domain`.`hosting_id` = `Hosting`.`id`)))
        join `config_service` `Service` ON ((`FTP`.`service_id` = `Service`.`id`)))
        join `config_server` `Server` ON ((`Service`.`server_id` = `Server`.`id`)))
