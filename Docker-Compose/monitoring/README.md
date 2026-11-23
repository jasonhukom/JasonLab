[← Back to Docker-Compose](../README.md)

# monitoring

> **Prometheus + Grafana + node_exporter**: collect metrics from your server and show them as dashboards.

## 🧩 What's in the stack

| Service | Port | Role |
| --- | --- | --- |
| `prometheus` | `9090` | Collects and stores metrics (config from `/etc/prometheus` on the host) |
| `grafana` | `3000` | Dashboards. Add Prometheus as a data source with the URL `http://prometheus:9090` |
| `node_exporter` | – | Publishes the host's CPU, memory, disk and network stats |

Prometheus and Grafana keep their data in Docker volumes.

## ✏️ Set up

1. Copy `prometheus.yml` (this folder) to `/etc/prometheus/prometheus.yml` on the host.
2. The file scrapes `prometheus` itself, `node_exporter:9100`, and a `cadvisor:8080` job. **cAdvisor isn't part of this compose file**, so remove that job or add the service.
3. Make sure the external network exists (see below).

## ▶️ Run it

```bash
docker network create your_network_name   # once, if it doesn't exist yet
docker compose up -d
docker compose logs -f
```
