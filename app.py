from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Url.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Url(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    old = db.Column(db.String(100))
    new = db.Column(db.String(100))

    def __init__(self, old, new):
        self.old = old
        self.new = new


@app.route("/", methods=["GET","POST"])
def index_route():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        found_url = Url.query.filter_by(old=request.form["url"]).first()
        if found_url:
            return render_template("result.html", original=found_url.old,new=found_url.new)
            
        else:
            old = request.form["url"]
            new = "This_is_a_brand_new_fuccin_url_innit?"
            url = Url(old=old,new=new)

            db.session.add(Url)
            db.session.commit()

        return render_template("result.html", original=url.old,new=url.new)

@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True) 