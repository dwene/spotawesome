from marshmallow import Schema
from exceptions import BadRequest

class Serializer(Schema):

    class Meta:
        strict = True

    def handle_error(self, errs, data):
        err = errs[0]
        raise BadRequest(err[err.keys()[0]][0], err)
