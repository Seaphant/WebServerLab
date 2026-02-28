#!/usr/bin/env python3
"""Capture screenshots for Web Server Lab submission."""

import subprocess
import time
import os

LAB_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    # Start the web server in background
    server = subprocess.Popen(
        ['python3', os.path.join(LAB_DIR, 'webserver.py')],
        cwd=LAB_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    
    # Wait for server to be ready
    time.sleep(1.5)
    
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': 1200, 'height': 800})
            
            # Screenshot 1: HelloWorld.html in browser
            page.goto('http://localhost:6789/HelloWorld.html', wait_until='networkidle')
            page.screenshot(path=os.path.join(LAB_DIR, 'screenshot_helloworld.png'))
            
            # Screenshot 2: 404 Not Found
            page.goto('http://localhost:6789/Nonexistent.html', wait_until='networkidle')
            page.screenshot(path=os.path.join(LAB_DIR, 'screenshot_404.png'))
            
            browser.close()
        
        print('Browser screenshots captured successfully.')
    except Exception as e:
        print(f'Error capturing screenshots: {e}')
    finally:
        server.terminate()
        server.wait(timeout=2)
    
    # Create terminal output for reference
    server2 = subprocess.Popen(
        ['python3', os.path.join(LAB_DIR, 'webserver.py')],
        cwd=LAB_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    time.sleep(1)
    server2.terminate()
    out, _ = server2.communicate(timeout=2)
    
    # Write terminal output to file for reference
    with open(os.path.join(LAB_DIR, 'terminal_output.txt'), 'w') as f:
        f.write(out or 'Ready to serve...')
    
    print('Screenshots complete.')

if __name__ == '__main__':
    main()
