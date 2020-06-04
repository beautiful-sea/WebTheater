from application.model.entity.video import Video
from flask import current_app

class VideoDAO:
    
    def __init__(self):
        self._videos = []
        self._videos.append(Video(1, "O QUE ACONTECE SE ZERAR O JOGO DO DINO SEM INTERNET?", "☛Zerando o jogo do dinossauro do google chrome.", "/videos/thumbs/dinossauros.jpg",'/videos/dinossauros.mp4',1,"02/04/2020"))
        self._videos.append(Video(2, "3 armadilhas das Negras na Abertura Cruz - Jogo de Damas", "Adquira os melhores softwares de análise do jogo de damas: Aurora Borealis e Edeon. Envie email para: aprendadamas@gmail.com", "/videos/thumbs/damas.jpg","/videos/damas.mp4",2,"02/04/2020"))
        self._videos.append(Video(3, "10 Invencoes Incriveis que Voce Nao Sabia que Existiam", "Só os loucos por tecnologia da um lik🤙", "/videos/thumbs/10invencoes.jpg","/videos/10invencoes.mp4",1,"02/04/2020"))
        self._videos.append(Video(4, "10 COISAS GENIAIS QUE VOCÊ PODE COMPRAR NA INTERNET", "Quem é que não gosta de invenções incríveis ou daquelas tecnologias impressionantes, não é mesmo? Bom o meu nome é Erick e esse é o Area Curiosa, e no vídeo de hoje você confere, 10 coisas geniais que você pode comprar na internet", "/videos/thumbs/10coisas.png","/videos/10coisas.mp4",2,"02/04/2020"))
       
    #BUSCA VIDEO PELO ID
    def get_video_by_id(self, id):
        video = None
        for index, item in enumerate(self.get_videos()):
            if item.get_id() == id:
                video = item
                return video
        return video
    
    #RETORNA TODOS VIDEOS
    def get_videos(self):
        return self._videos

    #RETORNA VIDEOS MAIS VISUALIZADOS
    def get_videos_most_likeds(self):
        videos = current_app.config['videos']
        most_likeds = sorted(videos.get_videos(), key=lambda x: x.get_qtd_likes(), reverse=True) #ORDENA USANDO SORTED E ITERA USANDO LAMBDA
        return most_likeds
    
    #BUSCA VIDEO PELO TITULO
    def search_videos(self, text_searched):
        return [i.__dict__ for i in self.get_videos() if  text_searched in i.get_title().upper() ]