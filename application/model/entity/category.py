from flask import current_app

class Category:

    def __init__(self, id, name, description,image):
        self._id = id
        self._name = name 
        self._description = description
        self._image = image

    def get_description (self):
        return self._description

    def get_image (self):
        return self._image

    def get_name (self):
        return self._name

    def set_id (self, id):
        self._id = id

    def get_id (self):
        return self._id
    
    def get_videos_by_category_id(self):
        videos = current_app.config['videos']
        videos_in_category = []
        for index, video in enumerate(videos.get_videos()):
            if video.get_id_category() == self.get_id():
                videos_in_category.append(video)
        return videos_in_category