from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "payment-service",
        "status": "running"
    })


@app.route("/payment/<int:order_id>")
def payment(order_id):

    return jsonify({
        "order_id": order_id,
        "payment_status": "success"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
