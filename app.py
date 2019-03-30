from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route("/<name>")
def say_hello_to(name):
  return render_template("index.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values

  return render_template("feedback.html", form_data=data)

  
app.run(debug=True)
