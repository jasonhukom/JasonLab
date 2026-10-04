[← Back to Docker-Compose](../README.md)

# n8n

> **n8n**: a workflow-automation tool. Connect apps and services visually, with webhooks, schedules and many integrations.

## 🧩 What's in the file

- Image `docker.n8n.io/n8nio/n8n`, `restart: always`, timezone `Asia/Jakarta`.
- Listens on `127.0.0.1:5678` (this machine only). Traffic comes in through **Traefik**, which is configured with the `traefik.*` labels (HTTPS, redirect and security headers). Traefik itself is *not* part of this repo.
- Workflow data lives in the `n8n_data` volume; `./local-files` is mounted at `/files` for workflows that read or write files.

## ✏️ Change before using

Replace the example hostname in `N8N_HOST`, `WEBHOOK_URL` and the Traefik labels with your own domain, and fill in your DNS server and network name.

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
