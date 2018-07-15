from .connect_database import BaseModel
from peewee import *
from .author_model import Author


class Paper(BaseModel):
    id = IntegerField(primary_key=True, null=False),
    author = ForeignKeyField(Author, to_field='id', null=False)
    title = TextField(null=False),
    abstract = TextField(null=False),
    publication = CharField(max_length=255, null=False),
    pub_date = DateField(null=False),
    source = CharField(max_length=255, null=False),
    doi = CharField(max_length=255, unique=True),
    arxiv_id = CharField(max_length=255, unique=True),
    scopus_id = CharField(max_length=255, unique=True),
    ads_id = CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'papers'
