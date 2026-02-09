CREATE USER '<mysql_username>'@'%' IDENTIFIED BY '<mysql_password>';
CREATE USER '<mysql_username>'@'phpmyadmin' IDENTIFIED BY '<mysql_password>';
GRANT ALL PRIVILEGES ON *.* TO '<mysql_username>'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO '<mysql_username>'@'phpmyadmin' WITH GRANT OPTION;
FLUSH PRIVILEGES;