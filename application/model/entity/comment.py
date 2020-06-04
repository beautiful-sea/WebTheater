

class Comment():

    def __init__(self,id,text, video_id):
        self._text = text
        self._video_id = video_id
        self._id = id

    def get_text(self):
        return self._text

    def get_id(self):
        return self._id

    def set_text(self, text):
        self._text = text
    
    def get_video_id(self):
        return self._video_id