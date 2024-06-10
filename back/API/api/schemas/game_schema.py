from api import ma
from marshmallow import Schema, fields

class LivroSchema(ma.Schema):
    class Meta:
        fields = ("_id", "titulo", "autor", "descricao", "ano")

    _id = fields.Str()
    titulo = fields.Str(required=True)
    autor = fields.Str(required=True)
    descricao = fields.Str(required=True)
    ano = fields.Int(required=True)
