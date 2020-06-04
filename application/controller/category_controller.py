from application import app
from flask import render_template, current_app
from application.model.dao.categoryDAO import CategoryDAO
import logging

@app.route("/category/<int:id>")
def category(id):
    category = current_app.config['categories'].get_category_by_id(id) #ENCONTRA A CATEGORIA DA PÁGINA PELO ID 
    videos   = category.get_videos_by_category_id() #OBTÉM OS VIDEOS PELO ID DA CATEGORIA
    return render_template("category.html", category = category, videos = videos)