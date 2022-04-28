from flask import Flask, render_template, request
import rag

app = Flask(__name__)

@app.route("/")
def index():
    article = rag.getArticle() 
    print(article)
    return render_template("index.html", article=article)

@app.route("/report")
def report():
    article = request.args.get("article")
    print("Reported article ", article)
    return render_template("report.html", article=article)
