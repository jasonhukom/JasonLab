[← Back to JasonLab](../README.md)

# Jason_Personal_Server

My Home Server

If you want a complete explanation on how to make one, go here <https://program.jasonhukom.my.id>

---

## 🏠 What is this?

A collection of **Docker Compose files** that together make up a self-hosted home server. Each service lives in its own folder with a `docker-compose.yaml` (or `.yml`) and a README.

## 🧩 Services

| Folder | What it is | Main ports |
| --- | --- | --- |
| [`9router/`](9router/README.md) | AI router (OpenAI-compatible endpoint) + its `headroom` companion | 20128, 8787 |
| [`adguardhome/`](adguardhome/README.md) | Network-wide DNS ad blocker | 53 (DNS) |
| [`bookstack/`](bookstack/README.md) | Wiki / documentation site | via proxy |
| [`cloudflared/`](cloudflared/README.md) | Cloudflare Tunnel (expose services without opening ports) | – |
| [`heimdall/`](heimdall/README.md) | Application dashboard / start page | 8080, 4443 |
| [`monitoring/`](monitoring/README.md) | Prometheus + Grafana + node_exporter | 9090, 3000 |
| [`mysql/`](mysql/README.md) | MariaDB database + phpMyAdmin | internal |
| [`n8n/`](n8n/README.md) | Workflow automation | 5678 (local) |
| [`netbird/`](netbird/README.md) | NetBird VPN client | – |
| [`nginx-proxy-manager/`](nginx-proxy-manager/README.md) | Reverse proxy with free HTTPS certificates | 80, 443 |
| [`wordpress/`](wordpress/README.md) | WordPress site | via proxy |

## ▶️ Using a stack

1. Install Docker with the Compose plugin.
2. Create the shared network the files expect (the name is a placeholder in most files):

   ```bash
   docker network create your_network_name
   ```

3. Open the folder you want, fill in the empty values (tokens, passwords, hostnames, DNS addresses).
4. Start it:

   ```bash
   docker compose up -d
   ```

5. Check on it with `docker compose ps` and `docker compose logs -f`.

## 🔐 Before you push to a public repo

- Replace every placeholder with your own value **locally**; don't commit real passwords, tokens or keys.
- A few files contain example passwords. Change them before running anything.
- The DNS entries (`192.168.x.x`) are addresses on a home network; change them to match yours.
