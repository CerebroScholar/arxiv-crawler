from .connect_database import BaseModel
from peewee import *
from .paper_model import Paper
from .author_model import Author


class PaperAuthor(BaseModel):
    paper_id = ForeignKeyField(Paper, null=False)
    author_id = ForeignKeyField(Author, null=False)

    class Meta:
        db_table = 'paper_authors'
        primary_key = CompositeKey('paper_id', 'author_id')
