from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myproject.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    text: Mapped[str] = mapped_column(String)

# with app.app_context():
#     db.create_all()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/create", methods=['POST','GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form[text]

        post = Post(title=title, text=text)
        try:
            db.session.add(post)
            db.session.commit()
            return render_template('/')
        except:
            return "Error"

    else:
        return render_template('create.html')    

if __name__ == "__main__":
    app.run(port=5001, debug=True)