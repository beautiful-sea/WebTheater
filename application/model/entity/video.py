import random
class Video:
    def __init__(self,id, title, description, thumb, file, id_category,created_at):
        self._id = id
        self._title = title
        self._description = description
        self._thumb = thumb
        self._file = file
        self._created_at = created_at
        self._id_category = id_category
        self._qtd_likes =  random.randint(0,100)
        self._qtd_views =  random.randint(100,10000)
        self._comments = []
    
    def get_id(self):
        return self._id

    def get_id_category(self):
        return self._id_category

    def get_created_at(self):
        return self._created_at

    def set_comment (self, commentary):
        self._comments.append (commentary)

    def set_qtd_likes (self, qtd_likes):
        self._qtd_likes = qtd_likes
    
    def set_qtd_views (self, qtd_views):
        self._qtd_views = qtd_views

    def get_comments (self):
        return self._comments
    
    def get_qtd_likes (self):
        return self._qtd_likes

    def get_qtd_views (self):
        return self._qtd_views

    def get_title (self):
        return self._title
    
    def get_description (self):
        return self._description 

    def get_thumb (self):
        return self._thumb

    def get_file (self):
        return self._file