from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('resume.html')

@app.route("/home")
def main_page():
    return render_template('home.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/projects")
def resume():
    return render_template('projects.html')

@app.route("/wip")
def resume():
    return render_template('wip.html')

@app.route("/pictures")
def resume():
    return render_template('pictures.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
