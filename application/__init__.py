from flask import Flask, session
import os
from application.model.dao.categoryDAO import CategoryDAO
from application.model.dao.videoDAO import VideoDAO
from application.model.dao.commentDAO import CommentDAO


app = Flask(
    __name__,
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/templates"),
)
categories   = CategoryDAO ()
videos       = VideoDAO ()
comments     = CommentDAO ()
app.config['categories'] = categories
app.config['videos']     = videos
app.config['comments']     = comments

from application.controller import comments_controller
from application.controller import home_controller
from application.controller import category_controller
from application.controller import video_controller
