from http.server import BaseHTTPRequestHandler, HTTPServer
from cart import calculate_total
import json
import argparse
import os
import sys


class ShopHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/cart/total":
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)
                cart_items = json.loads(body)
            except (ValueError, json.JSONDecodeError):
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "invalid JSON"}).encode())
                return

            total = calculate_total(cart_items)

            response = {
                "total": total
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())


def run_server(port: int):
    try:
        server = HTTPServer(("0.0.0.0", port), ShopHandler)
    except OSError as e:
        print(f"Server failed to start: {e}")
        sys.exit(1)

    print(f"Server running on port {port}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run demo and exit")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")), help="Port to bind the server")
    args = parser.parse_args()

    if args.demo:
        total = calculate_total(["apple"])
        print("Total Amount:", total)
        return

    run_server(args.port)


if __name__ == "__main__":
    main()
