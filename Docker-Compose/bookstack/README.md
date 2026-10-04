[← Back to Docker-Compose](../README.md)

# bookstack

> **BookStack**: a wiki-style site for writing and organising documentation, using the LinuxServer.io image.

## 🧩 What's in the file

- Image `lscr.io/linuxserver/bookstack:latest`, container name `jasonbookstack`.
- Needs a MySQL/MariaDB server, so run the [`mysql`](../mysql/README.md) stack first. `DB_HOST` points at the container `mysqldb`.
- Dark mode is on by default (`APP_DEFAULT_DARK_MODE`), timezone `Asia/Jakarta`.
- Config is kept in `./config`.
- No ports are published: reach it through a reverse proxy such as [nginx-proxy-manager](../nginx-proxy-manager/README.md).

## ✏️ Fill in before running

| Setting | What to put |
| --- | --- |
| `APP_URL` | The public address of your wiki |
| `APP_KEY` | Generate with `docker run -it --rm --entrypoint /bin/bash lscr.io/linuxserver/bookstack:latest appkey` |
| `DB_USERNAME`, `DB_PASSWORD`, `DB_DATABASE` | Credentials and database created in MySQL |
| `ALLOWED_IFRAME_SOURCES`, `ALLOWED_IFRAME_HOSTS` | Sites allowed to embed your wiki (or remove) |
| `dns`, `networks` | Your DNS server and external network name |

> 🔐 `DB_PASSWORD` currently holds a real-looking password. Replace it with a new one and keep it out of version control.

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
