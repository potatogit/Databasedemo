#!/usr/local/bin/python3
# 上面可以没有
import http.server
http.server.HTTPServer(("",8000),http.server.CGIHTTPRequestHandler).serve_forever()

