import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out" / "report.json"

class ReportHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/api", "/api/report"]:
            if not OUT.exists():
                self.send_error(404, "Report file not found")
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(OUT.read_bytes())
        else:
            self.send_error(404, "Endpoint not found")

def run(server_class=HTTPServer, handler_class=ReportHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"API Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()