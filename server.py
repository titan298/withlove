#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import sys

# Change to the blog directory
blog_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(blog_dir)

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"WithLove Blog server running at http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server")
            
            # Try to open the browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}')
            except:
                pass
                
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as e:
        if e.errno == 10048:  # Port already in use on Windows
            print(f"Port {PORT} is already in use. Please try a different port or stop the other server.")
        else:
            print(f"Error starting server: {e}")

if __name__ == "__main__":
    main()