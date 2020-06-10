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


if __name__ == '__main__':
    if User.table_exists() is False:
        User.create_table()

    # 1
    """
    user = User()
    user.username = 'Diego'
    user.password = 'password'
    user.email = 'dalvirdem@mail.com'
    user.save()
    """
    # 2
    """
    user = User(username='Josue', password='123456', email='jalvirdem@mail.com')
    user.save()
    """
    # 3
    """
    user = {'username': 'Eder', 'password': 'eder'}
    user = User(**user)
    user.save()
    """
    # 4
    #user = User.create(username='Armando', password='123456', email='armando@mail.com')
    # 5
    query = User.insert(username='Alondra', password='123456')
    query.execute()
