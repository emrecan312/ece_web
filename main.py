from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        message = request.form.get("message")
        if message:
            response = "Merhaba Emre 💙"
    return render_template("avatar.html", response=response)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
