
from flask import Flask

app = Flask("MyApp")

@app.route("/")
def hello():
  return "Hi Marc"

app.run(debug=True)
