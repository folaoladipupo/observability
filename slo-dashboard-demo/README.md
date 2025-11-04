# SLO Dashboard Demo

A demo SRE project showing how to measure, visualize, and track **API reliability (SLOs)** using **Prometheus + Grafana**.

## 🎯 Features
- Simulated API (Flask)
- Prometheus metrics:
  - `api_request_total`
  - `api_request_duration_seconds`
- Grafana dashboard with:
  - API Availability (%)
  - Latency (p95)
  - Error Budget Burn

## 🚀 Run Locally
```bash
docker compose up --build -d
```

- Mock API: [http://localhost:5000/api](http://localhost:5000/api)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000) (admin/admin)

## 📊 Queries

**Availability**
```promql
(sum(rate(api_request_total{status="success"}[5m])) / sum(rate(api_request_total[5m]))) * 100
```

**Latency (p95)**
```promql
histogram_quantile(0.95, sum(rate(api_request_duration_seconds_bucket[5m])) by (le))
```

**Error Budget Burn**
```promql
(1 - (sum(rate(api_request_total{status="success"}[5m])) / sum(rate(api_request_total[5m])))) * 100
```
