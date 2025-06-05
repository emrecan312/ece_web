from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        message = request.form.get("message")
        if message:
            response = "Merhaba Emre 💙 Ben buradayım canım. Mesajını aldım: " + message
    return render_template("avatar.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
