from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_name():
  return render_template('index.html', name="Jason")

app.run(debug=True)
