from application import app
import json
from flask import render_template, request, jsonify, current_app,Response
from application.model.dao.videoDAO import VideoDAO
from application.model.dao.categoryDAO import CategoryDAO
from application.model.entity.comment import Comment


#ROTA PARA BUSCAR OS VIDEOS NA HOME
@app.route("/video/search")
def search():
    try:
        text_searched = request.args.get('text').upper()    #TEXTO BUSCADO
        videos = current_app.config['videos']               #MODEL VIDEOS
        search = videos.search_videos(text_searched)        #BUSCA VIDEO NO MODEL
        return Response(json.dumps(search),  mimetype='application/json')
    except Exception as e:
        return str(e)

#ROTA PARA DAR LIKE NO VIDEO
@app.route("/video/like")
def like():
    try:
        videos = current_app.config['videos']           #MODEL DE VIDEOS INSTANCIADO
        id_video = int(request.args.get('id_video'))    #ID VIDEO RECEBIDO COMO PARAMETRO
        video = videos.get_video_by_id(id_video)        #ENCONTRANDO VIDEO 
        qtd_likes = (video.get_qtd_likes()) + 1         #DEFININDO QUANTIDADE DE LIKES
        video.set_qtd_likes(qtd_likes)                  #SETANDO LIKES
        return jsonify(qtd_likes = qtd_likes)
    except Exception as e:
        return str(e)

#ROTA PARA VISUALIZAR VIDEO ESPECIFICO
@app.route("/category/<int:id_category>/video/<int:id_video>")
def video(id_category,id_video):
    videos = current_app.config['videos']                                       #MODEL DE VIDEOS
    categories = current_app.config['categories']                               #MODEL DE CATEGORIAS
    comments = current_app.config['comments']                                   #MODEL DE COMENTARIOS
    video = videos.get_video_by_id(id_video)                                    #BUSCA VIDEO PELO ID
    video.set_qtd_views(video.get_qtd_views() + 1)                              #ADICIONA 1 VISUALIZACAO NO VIDEO
    comments_video = comments.find_comments_by_video_id(video.get_id())         #BUSCA COMENTARIOS PELO ID DO VIDEO
    category = categories.get_category_by_id(video.get_id_category())           #BUSCA CATEGORIAS PELO ID DO VIDEO
    return render_template("video.html", video = video,category=category, comments = comments_video)

