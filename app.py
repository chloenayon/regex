from flask import Flask, render_template, request, session
import google
import utils

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def start():
    session['has_answer'] = False
    if 'answer' not in session:
        session['answer'] = "John Cena"
    if request.method == "GET":
        return render_template("home.html", s = session)
    else:
        question = request.form['query']
        session['has_answer'] = True
        session['answer'] = str(utils.top_answers(question))
        return render_template("home.html", s = session)
    

if __name__=="__main__":
    app.debug = True
    app.secret_key = "dammit"
    app.run(host='0.0.0.0', port=8000)
