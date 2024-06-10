from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import livro_schema
from ..models import livro_model
from ..services import livro_service

class LivroList(Resource):
    def get(self):
        livros = livro_service.get_livros()
        l = livro_schema.LivroSchema(many=True)
        return make_response(l.jsonify(livros), 200)  # Código 200 (OK): Sucesso na solicitação.
    
    def post(self):
        l = livro_schema.LivroSchema()
        validate = l.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)  # Código 400 (BAD REQUEST): Solicitação inválida ou malformada.
        else:
            titulo = request.json["titulo"]
            autor = request.json["autor"]
            descricao = request.json["descricao"]
            ano = request.json["ano"]
            
            new_livro = livro_model.Livro(titulo=titulo, autor=autor, descricao=descricao, ano=ano)
            result = livro_service.add_livro(new_livro)
            res = l.jsonify(result)
            return make_response(res, 201)  # Código 201 (CREATED): Criação bem-sucedida de um novo recurso.
        
class LivroDetail(Resource):
    def get(self, id):
        livro = livro_service.get_livro_by_id(id)
        if livro is None:
            return make_response(jsonify("Livro não foi encontrado"), 404)  # Código 404 (NOT FOUND): Indica que o recurso requisitado não foi encontrado no servidor.
        l = livro_schema.LivroSchema()
        return make_response(l.jsonify(livro), 200)
    
    def put(self, id):
        livro_bd = livro_service.get_livro_by_id(id)
        if livro_bd is None:
            return make_response(jsonify("Livro não foi encontrado"), 404)
        l = livro_schema.LivroSchema()
        validate = l.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            titulo = request.json["titulo"]
            autor = request.json["autor"]
            descricao = request.json["descricao"]
            ano = request.json["ano"]
            new_livro = livro_model.Livro(titulo=titulo, autor=autor, descricao=descricao, ano=ano)
            livro_service.update_livro(new_livro, id)
            updated_livro = livro_service.get_livro_by_id(id)
            return make_response(l.jsonify(updated_livro), 200)
        
    def delete(self, id):
        livro_bd = livro_service.get_livro_by_id(id)
        if livro_bd is None:
            return make_response(jsonify("Livro não encontrado."), 404)
        livro_service.delete_livro(id)
        return make_response(jsonify("Livro excluído com sucesso!"), 204)  # Código 204 (NO CONTENT): Indica que a requisição foi bem sucedida, mas não há conteúdo para retornar ao cliente.
        
api.add_resource(LivroList, '/livros')
api.add_resource(LivroDetail, '/livros/<id>')
