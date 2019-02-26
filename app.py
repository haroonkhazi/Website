from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('resume.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/wip")
def wip():
    return render_template('wip.html')

@app.route("/pictures")
def pictures():
    return render_template('pictures.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
