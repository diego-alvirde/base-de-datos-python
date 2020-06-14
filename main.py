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
    user = peewee.ForeignKeyField(User, related_name='stores')
    name = peewee.CharField(max_length=50)
    addres = peewee.TextField()
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return self.name


class Product(peewee.Model):
    name = peewee.CharField(max_length=100)
    description = peewee.TextField()
    store = peewee.ForeignKeyField(Store, related_name='products')
    price = peewee.DecimalField(max_digits=5, decimal_places=2)  # 100.00
    stock = peewee.IntegerField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'products'

    def __str__(self):
        return '{name} - ${price}'.format(name=self.name, price=self.price)


def create_table():
    if Product.table_exists():
        Product.drop_table()
    if Store.table_exists():
        Store.drop_table()
    if User.table_exists():
        User.drop_table()

    User.create_table()
    Store.create_table()
    Product.create_table()


def insert_users():
    User.create(username='Diego', password='diego', email='diego@mail.com')
    User.create(username='Josue', password='josue', email='josue@mail.com')


def insert_stores():
    Store.create(user_id=1, name='Adidas', addres='Conocida')
    Store.create(user_id=2, name='Nike', addres='Conocida')


def insert_products():
    Product.create(store_id=1, name='Iniki', description='Tennis Iniki', price=100, stock=5)
    Product.create(store_id=1, name='Buzenits', description='Tennis Buzenits', price=100, stock=5)
    Product.create(store_id=1, name='Continental',
                   description='Tennis Continental', price=100, stock=5)

    Product.create(store_id=2, name='Air', description='Tennis Air', price=100, stock=5)
    Product.create(store_id=2, name='Jordan', description='Tennis Jordan', price=100, stock=5)
    Product.create(store_id=2, name='Venom', description='Tennis Venom', price=100, stock=5)


def create_schema():
    create_table()
    insert_users()
    insert_stores()
    insert_products()


if __name__ == '__main__':
    query = (
        Product.select()
        .join(Store)
        .join(User)
        .where(User.id == 1)
        .order_by(Product.price.desc())
    )

    for product in query:
        print(product)
