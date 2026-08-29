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
        "service": "order-service",
        "status": "running"
    })


@app.route("/orders")
def orders():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, product_id, quantity, status FROM orders"
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    orders_list = []

    for row in data:
        orders_list.append({
            "id": row[0],
            "product_id": row[1],
            "quantity": row[2],
            "status": row[3]
        })

    return jsonify({
        "orders": orders_list
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
