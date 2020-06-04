from application import app
from flask import render_template, current_app
from application.model.entity.video import Video
from application.model.dao.videoDAO import VideoDAO
from application.model.dao.categoryDAO import CategoryDAO

@app.route("/")
@app.route("/home")

def home():
    category_list = current_app.config['categories'].get_categories() #LISTA COM TODAS CATEGORIAS
    videos_most_likeds = current_app.config['videos'].get_videos_most_likeds() #LISTA COM VIDEOS MAIS CURTIDOS
    return render_template("home.html",category_list = category_list,videos_most_likeds=  videos_most_likeds)