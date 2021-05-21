from marshmallow import INCLUDE, Schema, fields, post_load

from mokkari import creator, team


class Character:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class CharacterSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    alias = fields.List(fields.Str)
    desc = fields.Str()
    wikipedia = fields.Str()
    image = fields.Url()
    creators = fields.Nested(creator.CreatorSchema, many=True)
    teams = fields.Nested(team.TeamSchema, many=True)

    class Meta:
        unknown = INCLUDE

    @post_load
    def make(self, data, **kwargs):
        return Character(**data)