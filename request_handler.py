from http.server import BaseHTTPRequestHandler
import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # Your code here