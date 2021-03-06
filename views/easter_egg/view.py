#this is where all the routes will go

from views.easter_egg import easter_egg_bp
from flask import Flask, render_template
from views.easter_egg import model


app = Flask(__name__)

@easter_egg_bp.route('/') #this is the home page of the makeup API page
def index():
    return render_template("easter_egg/home.html")

@easter_egg_bp.route('/theeastercontacts')
def eastercontactus():
    return render_template("easter_egg/newcontactus.html", images=model.infoforthecontactsineaster())

@easter_egg_bp.route('/image_map_dnhs')
def image_map():
    return render_template("easter_egg/image_map_dnhs.html", images=model.infoforthecontactsineaster())
