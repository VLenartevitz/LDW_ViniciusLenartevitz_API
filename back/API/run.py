from api import app, mongo
from api.models.livro_model import Livro
from api.services import livro_service

if __name__ == "__main__":
    with app.app_context():
        if 'livros' not in mongo.db.list_collection_names():
            livro = Livro(
                titulo='',
                autor='',
                descricao='',
                ano=0   
            )
            livro_service.add_livro(livro)
    app.run(debug=True)
