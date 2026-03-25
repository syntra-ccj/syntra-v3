import http.server, os, sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", port), handler)
print(f"Serving {root} on http://localhost:{port}")
httpd.serve_forever()
