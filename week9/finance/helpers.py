import requests
from flask import redirect, render_template, request, session
from functools import wraps

# Function to render apology messages
def apology(message, code=400):
    """Render message as an apology to the user."""
    def escape(s):
        """
        Escape special characters for URL-safe formatting.
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

# Decorator to require login on certain routes
def login_required(f):
    """
    Decorate routes to require login.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Function to lookup stock data based on symbol
def lookup(symbol):
    """Look up quote for symbol."""
    # Mock API response for testing
    if symbol == "TEST":
        return {
            "name": "Test Company",
            "price": 28.00
        }

    # Replace with actual API request
    API_TOKEN = 'c423fa4ec796476f854b72c3597c9a80'
    url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={API_TOKEN}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # Check if the data returned contains valid stock details
            if data:
                return {
                    "name": data.get("companyName"),
                    "price": data.get("latestPrice")
                }
            else:
                print(f"Invalid data returned for {symbol}: {data}")
                return None
    except Exception as e:
        print(f"Error during lookup: {e}")
    return None
