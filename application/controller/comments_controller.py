from application import app
from flask import render_template, current_app, request,jsonify,Response
from application.model.entity.video import Video
from application.model.dao.videoDAO import VideoDAO
from application.model.dao.categoryDAO import CategoryDAO
from application.model.dao.videoDAO import VideoDAO
from application.model.entity.comment import Comment

@app.route("/video/comment")
def comment():
    try:
        comments = current_app.config['comments']                                                                   # MODEL COMENTARIOS
        comments.ids_generateds +=1                                                                                 #GERA UM NOVO ID PARA O COMENTARIO
        comment = Comment(comments.ids_generateds,request.args.get('comment'),int(request.args.get('id_video')))    #CRIA COMENTARIO
        comments.add_comment(comment)                                                                               #ADICIONA COMENTARIO NO MODEL
        response = {'id':comment.get_id(), 'text':comment.get_text(), 'video_id': comment.get_video_id()} 
        return jsonify(response)
    except Exception as e:
        return str(e)


@app.route("/video/delete/")
def delete():
    try:
        comments = current_app.config['comments']                                       #MODEL DE COMENTARIOS
        delete = comments.delete_comment_by_id(int(request.args.get('id_comment')))     #DELETA COMENTARIO PELO ID
        if(delete == None):#SE O COMENTARIO NAO FOR ENCONTRADO:
            return jsonify(delete)
        return jsonify(True)
    except Exception as e:
        return str(e)