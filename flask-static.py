from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory(path)

@app.route('/')
def home():
   return render_template('home.html')

if __name__ == "__main__":
    app.run()