from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "api_request_total",
    "Total API requests",
    ["status"]
)

REQUEST_LATENCY = Histogram(
    "api_request_duration_seconds",
    "API request latency (seconds)",
    buckets=[0.05, 0.1, 0.3, 0.5, 1, 3, 5]
)

@app.route("/api")
def api():
    start = time.time()
    time.sleep(random.uniform(0.05, 0.5))
    if random.random() < 0.995:
        REQUEST_COUNT.labels(status="success").inc()
        status = "success"
        code = 200
    else:
        REQUEST_COUNT.labels(status="error").inc()
        status = "error"
        code = 500
    REQUEST_LATENCY.observe(time.time() - start)
    return jsonify({"status": status}), code

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
