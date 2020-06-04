from application.model.entity.category import Category
from application.model.entity.video import Video
from flask import current_app
import logging

class CategoryDAO():
    def __init__(self):
        self._categories= []
        self._categories.append(Category(1, "Jogos", "Teste Jogos","/categories/jogos.png"))
        self._categories.append(Category(2, "Tecnologia", "Teste Tecnologia","/categories/tecnologia.png"))
        self._categories.append(Category(3, "Saúde", "Teste de saúde","/categories/saude.png"))
    
    #RETORNA TODAS CATEGORIAS
    def get_categories(self):
        return self._categories

    #BUSCA CATEGORIA PELO ID
    def get_category_by_id(self, id):
        category = None
        for index, item in enumerate(self.get_categories()):
            if item.get_id() == id:
                category = item
                return category
        return category
