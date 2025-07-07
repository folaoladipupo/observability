# Docker Swarm Observability Stack

This repository sets up a full observability stack for Docker Swarm with:

- Prometheus
- Grafana
- Node Exporter
- Blackbox Exporter
- Alertmanager

## 📦 Services

| Service             | Port  |
|---------------------|-------|
| Prometheus          | 9090  |
| Grafana             | 3000  |
| Node Exporter       | 9100  |
| Blackbox Exporter   | 9115  |

## 🚀 Usage

```bash
docker stack deploy -c docker-compose.yml observability
```

## 📊 Dashboards

Import the `grafana_dashboard.json` in Grafana.

## 🔔 Alerts

Alerts for endpoint failures are defined in `alert-rules.yml`. Configure email in `alertmanager.yml`.

## 📝 Notes

Ensure SMTP credentials are updated in `alertmanager.yml`.
