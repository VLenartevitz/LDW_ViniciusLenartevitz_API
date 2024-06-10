from api import mongo
from ..models import livro_model
from bson import ObjectId

def add_livro(livro):
    mongo.db.livros.insert_one({
        'titulo': livro.titulo,
        'autor': livro.autor,
        'descricao': livro.descricao,
        'ano': livro.ano
    })

def get_livros():
    return list(mongo.db.livros.find())

def get_livro_by_id(id):
    return mongo.db.livros.find_one({'_id': ObjectId(id)})

def update_livro(id, livro):
    mongo.db.livros.update_one({'_id': ObjectId(id)},
    {'$set':
        {
        'titulo': livro.titulo,
        'autor': livro.autor,
        'descricao': livro.descricao,
        'ano': livro.ano
        }
    })

def delete_livro(id):
    mongo.db.livros.delete_one({'_id': ObjectId(id)})
