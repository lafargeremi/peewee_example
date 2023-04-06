import peewee as pw

DATABASE = 'example.db'
database = pw.SqliteDatabase(DATABASE)

class BaseModel(pw.Model):
    class Meta:
        database = database