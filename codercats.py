from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello_someone(name):
  return render_template("index.html", name=name.title())

app.run(debug=True)
