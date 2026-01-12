from http.server import BaseHTTPRequestHandler, HTTPServer
from cart import calculate_total
import json

class ShopHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/cart/total":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)

            cart_items = json.loads(body)
            total = calculate_total(cart_items)

            response = {
                "total": total
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

def run():
    server = HTTPServer(("0.0.0.0", 8000), ShopHandler)
    print("Server running on port 8000...")
    server.serve_forever()

if __name__ == "__main__":
    run()
