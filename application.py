from flask import *
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        global correct_answer
        global false_answer
        global numquestions
        correct_answer = 0
        false_answer = 0
        numquestions = abs(correct_answer) + abs(false_answer)
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")
        q4 = request.form.get("q4")
        q5 = request.form.get("q5")
        q6 = request.form.get("q6")
        q7 = request.form.get("q7")

        if q1 == "c":
            correct_answer = correct_answer + 1
        else:
            false_answer = false_answer + 1
        if q2 == "a":
            correct_answer = correct_answer + 1
        else:
            false_answer = false_answer + 1
        if q3 == "a":
            correct_answer = correct_answer + 1
        else:
            false_answer = false_answer + 1
        if q4 == "c":
            correct_answer = correct_answer + 1
        else:
            false_answer = false_answer + 1
        if q5 == "b":
            correct_answer = correct_answer + 1
        else:
            false_answer = false_answer + 1
        if q6 == "b":
            correct_answer == correct_answer + 1
        else:
            false_answer = false_answer + 1
        if q7 == "a":
            correct_answer = correct_answer + 1
        else:
            false_answer = false_answer + 1
        return render_template ("result.html", correct_answer = correct_answer)

    else:
        return render_template ("index.html")
