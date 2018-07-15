from .connect_database import BaseModel
from peewee import *


class Author(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255, null=False)

    class Meta:
        db_table = 'authors'
