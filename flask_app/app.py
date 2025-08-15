from flask import Flask, jsonify, request

app = Flask(__name__) 
products = [
    {"id": 1, "name": "Soap", "price": 25},
    {"id": 2, "name": "Shampoo", "price": 60}
]

@app.route('/products-12', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json() 
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products-entry/', methods=['PUT'])
def update_product():
    updated_data = request.get_json()
    print(updated_data)
    product_id = updated_data.get("id")
    for product in products:
        if product['id'] == product_id:
            product.update(updated_data)
            return jsonify(product)
    return {"error": "Product not found"}, 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return {"message": "Deleted successfully"}
    return {"error": "Product not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)
