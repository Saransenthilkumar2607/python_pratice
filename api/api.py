from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# In-memory data store
products = [
    {"id": 1, "name": "Soap", "price": 25},
    {"id": 2, "name": "Shampoo", "price": 60},
    {"id": 101, "name": "Toothpaste", "price": 45}
]

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def _parse_request_body(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length)
            return json.loads(body)
        return {}

    # GET: Get all products
    def do_GET(self):
        if self.path == "/products":
            self._set_headers()
            self.wfile.write(json.dumps(products).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    # POST: Add new product
    def do_POST(self):
        if self.path == "/products":
            new_product = self._parse_request_body()
            products.append(new_product)
            self._set_headers(201)
            self.wfile.write(json.dumps(new_product).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    # PUT: Update product
    def do_PUT(self):
        if self.path.startswith("/products/"):
            try:
                product_id = int(self.path.split("/")[-1])
            except ValueError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
                return

            updated_data = self._parse_request_body()
            for product in products:
                if product["id"] == product_id:
                    product.update(updated_data)
                    self._set_headers()
                    self.wfile.write(json.dumps(product).encode())
                    return

            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Product not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    # DELETE: Remove product
    def do_DELETE(self):
        if self.path.startswith("/products/"):
            try:
                product_id = int(self.path.split("/")[-1])
            except ValueError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid ID"}).encode())
                return

            for product in products:
                if product["id"] == product_id:
                    products.remove(product)
                    self._set_headers()
                    self.wfile.write(json.dumps({"message": "Deleted successfully"}).encode())
                    return

            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Product not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

def run(port=5000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f" Server running on http://127.0.0.1:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()