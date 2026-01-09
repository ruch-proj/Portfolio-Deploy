import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import your Flask app
from portfolio import app

# Vercel needs this
application = app
