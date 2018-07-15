import os
import settings
from peewee import MySQLDatabase, Model


# Connect to a MySQL database on network.
mysql_db = MySQLDatabase(
    settings.DATABASE_NAME,
    user=settings.DATABASE_USER,
    password=os.environ.get('DATABASE_PASSWORD'),
    host='localhost',
    port=os.environ.get('DATABASE_PORT')
)


class BaseModel(Model):
    class Meta:
        database = mysql_db
