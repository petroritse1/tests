from flask import Blueprint,redirect,render_template,flash,get_flashed_messages

view = Blueprint("view",__name__)


@view.route("/",methods=["POST","GET"])
def index():
    
    return render_template("home.html")
    