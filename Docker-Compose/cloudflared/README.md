[← Back to Docker-Compose](../README.md)

# cloudflared

> **Cloudflare Tunnel** client. Makes services on your server reachable from the internet through Cloudflare, **without opening any router ports**.

## 🧩 What's in the file

- Image `cloudflare/cloudflared:latest`, `restart: unless-stopped`.
- Runs `tunnel --no-autoupdate run`.
- The tunnel is identified by `TUNNEL_TOKEN`, which is empty in the file.
- Custom DNS entries and an external network keep it on the same network as your other containers.

## ✏️ Fill in before running

1. In the Cloudflare Zero Trust dashboard create a tunnel and copy its token.
2. Paste it as `TUNNEL_TOKEN` (never commit it).
3. Put your DNS server in `dns:` and your network name under `networks:`.
4. In the dashboard, point each public hostname at a service name on the shared network.

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
