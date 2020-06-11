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


if __name__ == '__main__':
    try:
        user = User.get(User.id == 39)
        print(user)
    except User.DoesNotExist as error:
        print("El usuario no existe")

    user = User.select().where(User.id == 3).first()
    if user:
        print("El usuario existe")
    else:
        print("El usuario no existe")

    count = User.select().where(User.id == 3).count()
    if(count):
        print("El usuario existe")
    else:
        print("El usuario no existe")

    flag = User.select().where(User.id == 3).exists()
    if(flag):
        print("El usuario existe")
    else:
        print("El usuario no existe")
