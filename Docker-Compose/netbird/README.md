[← Back to Docker-Compose](../README.md)

# netbird

> **NetBird client**: joins this server to your private NetBird network (a WireGuard-based mesh VPN) so your devices can reach it securely from anywhere.

## 🧩 What's in the file

- Image `netbirdio/netbird:latest`, container `netbird-client`, `restart: unless-stopped`.
- Extra Linux capabilities (`NET_ADMIN`, `SYS_MODULE`, `SYS_ADMIN`, `SYS_RESOURCE`) so it can create the VPN interface.
- Config in `./config`, state in `./netbird-data`.
- `NB_SETUP_KEY` enrols the machine; it is empty in the file.

## ✏️ Fill in before running

1. Create a **setup key** in the NetBird dashboard and put it in `NB_SETUP_KEY` (don't commit it).
2. Set `hostname` to the name this machine should have in NetBird.
3. Set the external network name.

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
