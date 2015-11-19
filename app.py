import flask from Flask, render_template, request
import google

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def start():
    if request.method = "GET":
        return render_template("home.html")
    else:
        return render_template("result.html")
