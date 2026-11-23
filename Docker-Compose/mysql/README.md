[← Back to Docker-Compose](../README.md)

# mysql

> **MariaDB 10.6 + phpMyAdmin**: the shared database server for other stacks such as [BookStack](../bookstack/README.md) and [WordPress](../wordpress/README.md).

## 🧩 What's in the stack

| Service | Container | Notes |
| --- | --- | --- |
| `mysqldb` | `mysqldb` | MariaDB, data in the `mysqldb` volume, runs `init.sql` on first start |
| `phpmyadmin` | `phpmyadmin` | Web UI. `PMA_ARBITRARY=1` lets you type any server name on the login page |

No ports are published; other containers reach the database as `mysqldb:3306` over the shared network, and you reach phpMyAdmin through a reverse proxy.

## ✏️ Fill in before running

- `MYSQL_ROOT_PASSWORD` in `docker-compose.yaml` is empty. Set it.
- `init.sql` has placeholders `<mysql_username>` and `<mysql_password>`. It creates that user (for any host and for phpMyAdmin) with **all privileges**, so choose a strong password.

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
