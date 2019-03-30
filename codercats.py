from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route("/<name>")
def say_hello_to(name):
  return render_template("index.html", user=name)

app.run(debug=True)
