from .connect_database import BaseModel
from peewee import *
from .paper_model import Paper


class Reference(BaseModel):
    subject_paper_id = ForeignKeyField(Paper, to_field='id', null=False)
    object_paper_id = ForeignKeyField(Paper, to_field='id', null=False)

    class Meta:
        db_table = 'refs'
        primary_key = CompositeKey('subject_paper_id', 'object_paper_id')
