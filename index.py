"""
Vercel wrapper for your portfolio.py
This file imports your original code without modifying it
"""

# Import your original Flask app
import sys
import os

# Add parent directory to path to import portfolio.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import everything from your original portfolio.py
from portfolio import app, HTML_TEMPLATE

# Create a simple handler for Vercel
def handler(request):
    from flask import Response
    
    # Create a test request context
    with app.test_request_context(path=request.get('path', '/')):
        # Get the response from your Flask app
        response = app.full_dispatch_request()
        
        # Convert Flask response to Vercel format
        return {
            'statusCode': response.status_code,
            'headers': {
                'Content-Type': response.content_type,
            },
            'body': response.get_data(as_text=True)
        }
