from ninja import Schema, ModelSchema
from targaryen.models import Person

class DragonOut(Schema):
    name: str
    birth_year: int