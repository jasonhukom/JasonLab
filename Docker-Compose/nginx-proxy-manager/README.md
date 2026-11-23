[← Back to Docker-Compose](../README.md)

# nginx-proxy-manager

> **Nginx Proxy Manager**: a web UI for reverse proxying. Point domain names at your internal services and get free HTTPS certificates from Let's Encrypt.

## 🧩 What's in the file

- Image `jc21/nginx-proxy-manager:latest`, container `npm`, `restart: unless-stopped`.
- Ports **80** (HTTP) and **443** (HTTPS) are published.
- The admin UI port **81** is *commented out*. Uncomment `- "81:81"` for the first-time setup, then log in at `http://<server-ip>:81`.
- Settings in `./data`, certificates in `./letsencrypt`.
- Uses local DNS servers and the external network.

Other stacks (BookStack, WordPress, phpMyAdmin, n8n…) don't publish ports; add a *Proxy Host* here that points to the container name on the shared network.

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
