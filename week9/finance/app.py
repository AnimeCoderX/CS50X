from flask import Flask, render_template, request, redirect, url_for, flash, session
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import apology, lookup
import re

# Initialize Flask app and database connection
app = Flask(__name__)
app.secret_key = 'c423fa4ec796476f854b72c3597c9a80'  # Set a secret key for session management
db = SQL("sqlite:///finance.db")  # Connect to the database

# Home route - If user is logged in, show quote page, else redirect to login


@app.route("/")
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))

    # Fetch user data
    user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

    if len(user_info) == 0:
        return redirect(url_for("logout"))

    # Example of fetching user-specific data (customize this as needed)
    user = user_info[0]
    return render_template("quote.html", user=user)

# Add the custom 404 error handler at the bottom of your route definitions


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Finally, this block should be at the end
if __name__ == "__main__":
    app.run(debug=True)
# Registration route - handles user signup and validation


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Clear any previous session data (if logged in previously)
    session.clear()

    # If the request is GET, render the registration form
    if request.method == "GET":
        return render_template("register.html")

    # If the request is POST, process the registration data
    else:
        # Get the form data from the POST request
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate the username
        if not username:
            return render_template("register.html", error="Please provide a username"), 400

        # Validate the password (check for empty password)
        if not password:
            return render_template("register.html", error="Please provide a password"), 400

        # Validate the confirmation password (check for empty confirmation password)
        if not confirmation:
            return render_template("register.html", error="Please confirm your password"), 400

        # Check if the password and confirmation match
        if password != confirmation:
            return render_template("register.html", error="Passwords do not match"), 400

        # Check if the username is already taken
        user_check = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(user_check) > 0:
            return render_template("register.html", error="Username is already taken"), 400

        # Password strength validation (at least 8 characters, 1 number, 1 uppercase, 1 special character)
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            return render_template("register.html", error="Password must be at least 8 characters long, contain a number, an uppercase letter, and a special character"), 400

        # Hash the password securely
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # Insert the new user into the database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashed_password)

        # Flash a success message and redirect the user to the login page
        flash("You have successfully registered! Please log in.", "success")
        return redirect(url_for("login"))


# Login route - handles user login and session management
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if user exists in database
        user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(user) == 0 or not check_password_hash(user[0]["hash"], password):
            flash("Invalid username or password", "danger")
            return redirect(url_for("login"))

        # Store user session
        session["user_id"] = user[0]["id"]
        flash("Login successful!", "success")
        return redirect(url_for("index"))

    return render_template("login.html")

# Quote route - user-specific quote page after login


@app.route("/quote", methods=["GET", "POST"])
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Validate the input
        if not symbol:
            return render_template("apology.html", top=400, bottom="Ticker symbol cannot be blank"), 400

        # Use the lookup function to get stock data
        stock = lookup(symbol)

        # Debugging: Print the stock data to verify what is being returned
        print(f"Stock data for symbol '{symbol}': {stock}")

        # Check if the stock was found
        if stock:
            return render_template("quote.html", stock=stock)  # Render with stock data
        else:
            # Render error page
            return render_template("apology.html", top=400, bottom="Invalid stock symbol"), 400  # Render error page

    return render_template("quote.html")

# Account Settings route - allows users to update their information


@app.route("/account", methods=["GET", "POST"])
def account():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        new_username = request.form.get("username")
        new_password = request.form.get("new_password")
        confirm_new_password = request.form.get("confirm_new_password")

        if new_password != confirm_new_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("account"))

        # Validate new password strength
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', new_password):
            flash("Password must be at least 8 characters long, contain a number, an uppercase letter, and a special character.", "danger")
            return redirect(url_for("account"))

        hashed_password = generate_password_hash(new_password)

        # Update user details in database
        db.execute("UPDATE users SET username = ?, hash = ? WHERE id = ?",
                   new_username, hashed_password, session["user_id"])

        flash("Account updated successfully!", "success")
        return redirect(url_for("index"))

    user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    return render_template("account.html", user=user_info[0])


@app.route("/buy", methods=["GET", "POST"])
def buy():
    """Buy stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate the ticker symbol
        if not symbol:
            return render_template("apology.html", top=400, bottom="Ticker symbol cannot be blank"), 400

        # Use the lookup function to get stock data
        stock = lookup(symbol)

        # Check if the stock was found
        if not stock:
            return render_template("apology.html", top=400, bottom="Invalid stock symbol"), 400

        # Validate the shares input (should be a positive integer)
        if not shares or not shares.isdigit() or int(shares) <= 0:
            return render_template("apology.html", top=400, bottom="Shares must be a positive integer"), 400

        # Calculate the total price of the purchase
        total_price = stock["price"] * int(shares)

        # Fetch the user's cash balance
        user_info = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        if len(user_info) == 0:
            return render_template("apology.html", top=400, bottom="User not found"), 400
        cash = user_info[0]["cash"]

        # Check if the user has enough cash to buy the stock
        if total_price > cash:
            return render_template("apology.html", top=400, bottom="You do not have enough cash to make this purchase"), 400

        # Proceed with the purchase (subtract cash and add shares to user's portfolio)
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_price, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], symbol, int(shares), stock["price"])

        # Return a success message (or render the purchase confirmation page)
        return render_template("purchase_confirmation.html", stock=stock, shares=shares, total_price=total_price)

    return render_template("buy.html")


# Helper route to show user data for debugging purposes
@app.route("/debug")
def debug():
    if "user_id" not in session:
        return redirect(url_for("login"))

    # Fetch all user data for debugging
    users = db.execute("SELECT * FROM users")
    return render_template("debug.html", users=users)

# Error handling route - custom error page for 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling route - custom error page for 500


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Running the Flask application
if __name__ == "__main__":
    app.run(debug=True)
