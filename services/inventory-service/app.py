from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "inventory-service",
        "status": "running"
    })


@app.route("/inventory/<product>")
def inventory(product):

    return jsonify({
        "product": product,
        "stock": 10,
        "available": True
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
