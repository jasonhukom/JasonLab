[← Back to Docker-Compose](../README.md)

# wordpress

> **WordPress**: the website and blog engine, using the official image.

## 🧩 What's in the file

- Image `wordpress`, container `wordpress`, `restart: always`.
- Site files persist in the `wordpress` volume.
- Needs an external database. Use the [`mysql`](../mysql/README.md) stack.
- No ports are published: serve it through [nginx-proxy-manager](../nginx-proxy-manager/README.md).

## ✏️ Fill in before running

| Variable | Value |
| --- | --- |
| `WORDPRESS_DB_HOST` | `mysqldb` (the MariaDB container name) |
| `WORDPRESS_DB_USER` / `WORDPRESS_DB_PASSWORD` | The MySQL user you created for WordPress |
| `WORDPRESS_DB_NAME` | An empty database you created for it |

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
