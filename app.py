from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('firstdt.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

app.run(host='0.0.0.0', port=5000, debug=True)