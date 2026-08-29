from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="172.31.41.109",
        database="cloudmartdb",
        user="cloudmart",
        password="password123"
    )
    return conn


@app.route("/")
def home():
    return jsonify({
        "service": "payment-service",
        "status": "running"
    })


@app.route("/payment/<int:order_id>")
def payment(order_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT order_id, amount, status FROM payments WHERE order_id=%s",
        (order_id,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify({
            "order_id": result[0],
            "amount": result[1],
            "payment_status": result[2]
        })

    return jsonify({
        "order_id": order_id,
        "payment_status": "not found"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
