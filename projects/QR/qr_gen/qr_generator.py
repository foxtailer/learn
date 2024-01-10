from flask import Flask,request,render_template
import qrcode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("E:\GIT\learn\projects\QR\qr_gen\teemplate\index.html")

if __name__ == "__main__":
    app.run(debug=True)

