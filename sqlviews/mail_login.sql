CREATE VIEW `mail_login` AS
    select 
        `User`.`username` AS `user`,
        `Account`.`password` AS `password`,
        concat(`Server`.`home_base`,
                '/',
                `Hosting`.`name`,
                '/mail/',
                `Account`.`username`) AS `home`,
        concat(`Server`.`home_base`,
                '/',
                `Hosting`.`name`,
                '/mail/',
                `Account`.`username`,
                '/Maildir') AS `mail`,
        (`Server`.`uid_base` + `Account`.`id`) AS `uid`,
        (`Server`.`gid_base` + `Hosting`.`id`) AS `gid`,
        `Service`.`name` AS `service`
    from
        (((((((`maildomain_mailbox` `Mailbox`
        join `maildomain_maildomain` `Maildomain` ON ((`Mailbox`.`domain_id` = `Maildomain`.`id`)))
        join `account_account` `Account` ON ((`Mailbox`.`username_id` = `Account`.`id`)))
        join `auth_user` `User` ON ((`Account`.`adminuser_id` = `User`.`id`)))
        join `domain_domain` `Domain` ON ((`Account`.`domain_id` = `Domain`.`id`)))
        join `hosting_hosting` `Hosting` ON ((`Domain`.`hosting_id` = `Hosting`.`id`)))
        join `config_service` `Service` ON ((`Maildomain`.`service_id` = `Service`.`id`)))
        join `config_server` `Server` ON ((`Service`.`server_id` = `Server`.`id`)))
