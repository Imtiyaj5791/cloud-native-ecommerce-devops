from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)


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
        "service": "inventory-service",
        "status": "running"
    })


# Get all products
@app.route("/products")
def products():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, price, stock FROM products"
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    products_list = []

    for row in data:
        products_list.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "stock": row[3]
        })

    return jsonify(products_list)



# Check single product inventory
@app.route("/inventory/<product>")
def inventory(product):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, stock FROM products WHERE name=%s",
        (product,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify({
            "product": result[0],
            "stock": result[1],
            "available": result[1] > 0
        })

    return jsonify({
        "product": product,
        "available": False,
        "message": "Product not found"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
