[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5fV5Rrzc)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16764947)
# My First Web Server

To reinforce your understanding of HTTP, we will be creating an *extremely* basic web server using Python. This server will only respond to `GET` requests (the default requests made by web browsers), and will provide a simple interface for understanding how HTTP requests and responses work.

## Requirements

Your assignment is to complete the `do_GET` method in the `request_handler.py` module to handle `GET` requests and return the appropriate response. Your program should also adhere to the following criteria:

- Use Python's built-in `http.server` module
- The server will listen on `localhost`, port `8000` by default
- Implement a custom request handler that responds to all `GET` requests with the current day of the week in title-case formatting (i.e. `Wednesday`)
- Return a `200 OK` status code with the response
- Include a custom header called `X-Joke` with your *best* joke (i.e. `I made a pencil with two erasers. It was pointless.`)

## Extra Credit

For 10 points extra credit on this assignment, add support for a `POST` request that echoes the body of the request (i.e. if you `POST` the message `Hello, World!`, the response should be `Hello, World!`).

## Testing

To test your server, run the following command from within the project directory:

```python
python3 server.py
```

This will start the server up on port `8000`. You can access your server by visiting http://localhost:8000 in your web browser or by using a tool like cURL. To test with cURL, you can use the following command:

```bash
curl -v http://localhost:8000
```

This will display the full HTTP request and response, allowing you to verify that your server is functioning correctly and returning the expected day of the week along with your custom header.

## Resources

- [Python's http.server Documentation](https://docs.python.org/3/library/http.server.html)
- [Python's `datetime` Module](https://docs.python.org/3/library/datetime.html)
- [HTTP Status Codes](https://httpstatuses.com/)
- [cURL Documentation](https://curl.haxx.se/docs/manpage.html)