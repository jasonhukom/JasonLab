[← Back to Docker-Compose](../README.md)

# heimdall

> **Heimdall**: a start page / dashboard with a tile for each of your self-hosted apps.

## 🧩 What's in the file

- Image `lscr.io/linuxserver/heimdall:latest`, container name `heimdall`.
- Ports: **8080 → 80** (HTTP) and **4443 → 443** (HTTPS).
- `PUID`/`PGID` 1000, timezone `Asia/Jakarta`, `ALLOW_INTERNAL_REQUESTS=true`.
- Config volume `/path/to/heimdall/config` is a placeholder. Change it to a real folder.
- Uses two DNS servers (a local one and the router) and the external network `jasonhukom`.

Open `http://<server-ip>:8080` once it's running.

## ▶️ Run it

```bash
docker network create jasonhukom   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
