# Web Server Lab

A simple HTTP Web Server implementation in Python using TCP socket programming. This lab implements a basic web server that handles one HTTP request at a time, serves HTML files, and returns 404 for non-existent resources.

## Requirements

- Python 3.x

## Files

- `webserver.py` - The complete web server implementation
- `HelloWorld.html` - Test HTML file served by the server

## How to Run

1. Start the web server:
   ```bash
   python3 webserver.py
   ```

2. Open a web browser and navigate to:
   - `http://localhost:6789/HelloWorld.html` - To view the test page
   - `http://localhost:6789/Nonexistent.html` - To test 404 response

3. Or use your machine's IP address when testing from another host:
   - `http://YOUR_IP:6789/HelloWorld.html`

## Features

- Listens on port 6789
- Serves static HTML files from the current directory
- Returns `200 OK` with file contents for valid requests
- Returns `404 Not Found` for non-existent files
- Uses standard HTTP/1.1 response format

## Submission

See `WebServer_Lab_Submission.docx` for the lab report with screenshots demonstrating each step.
