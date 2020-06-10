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
    # user = User.select().where(User.id == 3).get()  # Obtiene el primer usuario
    # user = User.select().where(User.email >> None).get()  # null
    # user = User.select().where(~User.email >> None).get()  # not null
    # SELECT * FROM users WHERE username in (datos)
    users = ['Eder', 'Alondra']
    users = User.select().where(User.username << users)
    for user in users:
        print(user)

    # SELECT * FROM users WHERE username like 'texto%' .startswith
    # SELECT * FROM users WHERE username like 'texto%' .endwith
    # SELECT * FROM users WHERE username like '%texto%'
    users = User.select().where(User.username.contains('Eder'))
    for user in users:
        print(user)
    # for user in users:
    #    print(user)
