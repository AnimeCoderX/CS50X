from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    try:
        name = request.form.get("name")
        sport = request.form.get("sport")

        if not name or sport not in SPORTS:
            return render_template("failure.html")

        # Save data to a .txt file
        with open("registrations.txt", "a") as file:
            file.write(f"Name: {name}, Sport: {sport}\n")

        return render_template("success.html")
    except Exception as e:
        return f"An error occurred: {e}", 500

# Admin route to view registrations
@app.route("/admin")
def admin():
    try:
        with open("registrations.txt", "r") as file:
            data = file.readlines()
        return "<br>".join(data)
    except FileNotFoundError:
        return "No registrations found.", 404

if __name__ == "__main__":
    app.run(debug=True)
