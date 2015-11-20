from flask import Flask, render_template, request
import google
import utils

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def start():
    if request.method == "GET":
        return render_template("home.html")
    else:
        question = request.form['query']
        r = utils.top_names(question)
        return render_template("result.html", r = r)
    

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
