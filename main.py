from flask import Flask, render_template, request
app = Flask(__name__)
import random
import string
app.config['DEBUG'] = True

@app.route("/", methods=["GET", "POST"])
def index():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    plen = 8
    length = request.form.get("length")
    if length == None:
        length = 8
    else:
        plen = int(length)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    passcode = ("".join(s[0:plen]))
    return render_template("index.html", passcode = passcode)

if __name__ == "__main__":
    app.run()