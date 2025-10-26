from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    # 例
    diary_titles = ["今日の散歩", "読書メモ", "晩ごはん記録"]
    return render_template("index.html", titles=diary_titles)