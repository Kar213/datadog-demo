from flask import Flask, request
import logging
import sys

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")
    return {"message": "Welcome to Demo Portal with Datadog"}

@app.route("/update", methods=["POST"])
def update_user():
    data = request.json
    app.logger.info(f"User updated: {data}")
    return {"status": "ok", "data": data}

@app.route("/error")
def error():
    app.logger.error("Simulated error occurred!")
    return {"status": "error"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
