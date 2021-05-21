from marshmallow import INCLUDE, Schema, fields, post_load


class Publisher:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class PublisherSchema(Schema):
    id = fields.Int()
    founded = fields.Int()
    desc = fields.Str()
    wikipedia = fields.Str()
    image = fields.Url()

    class Meta:
        unknown = INCLUDE

    @post_load
    def make(self, data, **kwargs):
        return Publisher(**data)