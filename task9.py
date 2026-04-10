from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  
    data = ["Иван", "Мария", "Алексей"]
    return render_template("index.html", users=data)

app.run()