import flask from Flask, render_template, request
import google

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def start():
    if request.method = "GET":
        return render_template("home.html")
    else:
        question = request.form['query']
        print question
        return render_template("result.html")
    

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
