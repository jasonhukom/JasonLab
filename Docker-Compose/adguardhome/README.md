[← Back to Docker-Compose](../README.md)

# AdGuardHome

*AdGuardHome dockercompose.yaml README*

Open the initial setup wizard and admin UI HTTP

```yaml
  ports:
      #--- Listining Ports ---
      - "53:53/tcp"       # DNS
      - "53:53/udp"       # DNS
      - "3000:3000/tcp"   # Initial Setup Wizzard
      - "8080:80/tcp"   # Admin UI HTTP
```

---

## 🛡️ What is this?

[AdGuard Home](https://adguard.com/adguard-home.html) is a DNS server that blocks ads and trackers for every device on your network. This folder runs it in Docker.

## ⚙️ How it works

- Image: `adguard/adguardhome:latest`, container name `adguardhome`, `restart: unless-stopped`.
- Port **53** (TCP + UDP) is published for DNS.
- The two lines for the **setup wizard (3000)** and **admin UI (8080 → 80)** are *commented out* in `docker-compose.yaml`. Uncomment them, as in the snippet above, to reach the wizard and the admin page.
- Data is stored next to the compose file in `./workdir` and `./confdir`.
- Joins an external network called `your_network_name` (placeholder, create it first).

## ▶️ Run it

```bash
docker network create your_network_name
docker compose up -d
```

Then open `http://<server-ip>:3000` for the first-time setup, and afterwards the admin UI on port 8080. Once set up you can comment the two lines out again.
