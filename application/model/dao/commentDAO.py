from application.model.entity.comment import Comment
from flask import current_app

class CommentDAO():
    def __init__(self):
        self._comments= []
        self.ids_generateds = 1
    
    #RETORNA TODOS COMENTARIOS
    def get_comments(self):
        return self._comments
    
    #ADICIONA UM NOVO COMENTARIO
    def add_comment(self, comment):
        self._comments.append(comment)

    #BUSCA COMENTARIO PELO ID DO VIDEO
    def find_comments_by_video_id(self, id_video):
        comments = current_app.config['comments']
        comments_video = []
        for i, comment in enumerate(comments.get_comments()):
            if comment.get_video_id() == id_video:
                comments_video.append(comment)
        return comments_video
    
    #DELETA COMENTARIO PELO ID
    def delete_comment_by_id(self,id_comment):
        comments = current_app.config['comments']
        for i, comment in enumerate(comments.get_comments()):
            if comment.get_id() == id_comment:
                self._comments.pop(i)
                return comment
        return None