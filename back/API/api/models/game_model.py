from api import mongo

class Game:
    def __init__(self, titulo, descricao, ano):
        self.titulo = titulo
        self.descricao = descricao
        self.ano = ano

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "ano": self.ano
        }
