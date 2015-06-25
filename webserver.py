#import http.server
#http.server.HTTPServer(("",8000),http.server.CGIHTTPRequestHandler).serve_forever()
import SimpleHTTPServer,CGIHTTPServer

Handler = CGIHTTPServer.CGIHTTPRequestHandler
SimpleHTTPServer(("", 8000), Handler).serve_forever()
