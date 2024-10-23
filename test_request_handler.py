# test_request_handler.py
import pytest
from unittest.mock import Mock, patch
from io import BytesIO
from request_handler import SimpleHTTPRequestHandler
import datetime

def test_do_GET():
    # Mock the request and response objects
    request = Mock()
    request.makefile.return_value = BytesIO(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

    response = BytesIO()

    handler = SimpleHTTPRequestHandler(request, ('localhost', 0), Mock())
    handler.wfile = response

    headers = {}

    # Patch the send_response and send_header methods to capture headers
    with patch.object(handler, 'send_response') as mock_send_response, \
         patch.object(handler, 'send_header') as mock_send_header:

        def capture_header(key, value):
            headers[key] = value

        mock_send_header.side_effect = capture_header

        # Call the do_GET method
        handler.do_GET()

        # Verify the status code
        mock_send_response.assert_called_once_with(200)

        # Verify the headers
        # only make sure x-joke is included, the value can be anything
        assert 'X-Joke' in headers

    # Verify the body
    response.seek(0)
    body = response.read().decode('utf-8').strip()
    assert datetime.datetime.now().strftime("%A") in body
