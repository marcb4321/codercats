from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_someone():
  return render_template("index.html", name=name.title())

app.run(debug=True)
