[← Back to Docker-Compose](../README.md)

# 9router

> **9router** is a self-hosted *AI router*: one OpenAI-compatible API endpoint in front of many AI model providers. This stack runs it together with a companion service called **headroom**.

## 🧩 What's in the file

| Service | Image | Port | Notes |
| --- | --- | --- | --- |
| `9router` | `decolua/9router:latest` | `20128` | Dashboard and API. Data is stored in `$HOME/.9router` on the host (mounted at `/app/data`) |
| `headroom` | `ghcr.io/chopratejas/headroom:latest` | `8787` | Companion service; 9router reaches it through `HEADROOM_URL` |

`9router` starts after `headroom` and joins the external network `jasonhukom` (rename it to your own).

## 🔐 Before you start

`INITIAL_PASSWORD` in the compose file is only a simple example value. **Set your own strong password** (ideally from an `.env` file that isn't committed) before exposing the port.

## ▶️ Run it

```bash
docker network create jasonhukom   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
