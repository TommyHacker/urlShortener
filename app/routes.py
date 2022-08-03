from flask import render_template, request, redirect
from app import app , db
from app.models import Urls
import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



@app.route("/", methods=["GET","POST"])
def index_route():
    if request.method == "GET":
        return render_template("index.html")
    else:
        old = request.form["url"]
        found_url = Urls.query.filter_by(old_url=old).first()
        if found_url == None:
            new = id_generator()
            newUrl = Urls(old_url=old,new_url=new)
            db.session.add(newUrl)
            db.session.commit()

            return render_template("result.html",original=old,new=new)
        else:
            print(found_url)
            return render_template("result.html",original=found_url.old_url,new=found_url.new_url)

@app.route("/<id>",methods=["GET"])
def reroute(id):
    url = Urls.query.filter_by(new_url=id).first()
    return redirect(f"http://{url.old_url}")
