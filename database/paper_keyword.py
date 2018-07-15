from .connect_database import BaseModel
from peewee import *
from .paper_model import Paper


class PaperKeyword(BaseModel):
    paper_id = ForeignKeyField(Paper, null=False)
    keyword = CharField(max_length=255, null=False)

    class Meta:
        db_table = 'paper_keywords'
        primary_key = CompositeKey('paper_id', 'keyword')
