"""
Vercel handler - imports your portfolio
"""

# Import your Flask app from portfolio.py
from portfolio import app

# Vercel requires this to be called 'application'
application = app
