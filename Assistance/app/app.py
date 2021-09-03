from flask import Flask, render_template, request
from flask import redirect,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/index", methods=["post"])
def translate():
    #翻訳ボタンを押した際の処理
    if "translate" in request.form:
        code = request.form["code"]
        return render_template("index.html", code=code, transcode=code)

    #評価ボタンを押した際の処理
    elif "good" in request.form:
        transcode = request.form["transcode"]
        return render_template("index.html", code=transcode, transcode=transcode)



if __name__ == "__main__":
    app.run(debug=True)