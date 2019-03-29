from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
  return "Hi Marc"

@app.route("/<name>")
def hello_someone(name):
  return render_template("hello.html", name=name.title())

app.run(debug=True)
