import peewee
import datetime

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'minicurso_python'

database = peewee.MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, password=PASSWORD)


class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50, null=True)
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'

    def __str__(self):
        return self.username


class Store(peewee.Model):
    user = peewee.ForeignKeyField(User, primary_key=True)
    name = peewee.CharField(max_length=50)
    addres = peewee.TextField()
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return self.name


if __name__ == '__main__':
    """
    if Store.table_exists():
        Store.drop_table()
    if User.table_exists():
        User.drop_table()
    User.create_table()
    Store.create_table()

    user = User.create(username='Diego', password='diego', email='diego@mail.com')
    store = Store.create(name='Adidas', addres='Conocida', user=user)
    """
    tienda = Store.get(Store.user_id == 1)
    print(tienda)
    print(tienda.user)
