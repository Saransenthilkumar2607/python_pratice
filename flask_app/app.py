from flask import Flask, jsonify, request

app = Flask(__name__)  # Create the Flask app

# Sample Data (like from a database)
products = [
    {"id": 1, "name": "Soap", "price": 25},
    {"id": 2, "name": "Shampoo", "price": 60}
]

# GET: Fetch all products
@app.route('/products-12', methods=['GET'])
def get_products():
    return jsonify(products)

# POST: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()  # Get JSON data from user
    products.append(new_product)
    return jsonify(new_product), 201

# PUT: Update a product (full update)
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_data = request.get_json()
    for product in products:
        if product['id'] == product_id:
            product.update(updated_data)
            return jsonify(product)
    return {"error": "Product not found"}, 404

# DELETE: Remove a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return {"message": "Deleted successfully"}
    return {"error": "Product not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)