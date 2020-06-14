import peewee
from models import (User, Store, Product, Category, CategoriesProduct)


def create_table():
    if CategoriesProduct.table_exists():
        CategoriesProduct.drop_table()
    if Category.table_exists():
        Category.drop_table()
    if Product.table_exists():
        Product.drop_table()
    if Store.table_exists():
        Store.drop_table()
    if User.table_exists():
        User.drop_table()

    User.create_table()
    Store.create_table()
    Product.create_table()
    Category.create_table()
    CategoriesProduct.create_table()


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


def insert_categories():
    Category.create(name='Liquidos', description='liquidos')
    Category.create(name='Embutidos', description='embutidos')
    Category.create(name='Snacks', description='snacks')
    Category.create(name='Aderezos', description='aderezos')
    Category.create(name='Carnes', description='carnes')


def insert_categories_product():
    CategoriesProduct.create(category_id=1, product_id=5)
    CategoriesProduct.create(category_id=1, product_id=5)
    CategoriesProduct.create(category_id=1, product_id=5)

    CategoriesProduct.create(category_id=2, product_id=4)

    CategoriesProduct.create(category_id=3, product_id=3)

    CategoriesProduct.create(category_id=4, product_id=2)
    CategoriesProduct.create(category_id=4, product_id=2)

    CategoriesProduct.create(category_id=5, product_id=1)


def create_schema():
    create_table()
    insert_users()
    insert_stores()
    insert_products()
    insert_categories()
    insert_categories_product()


if __name__ == '__main__':
    categories = Category.select()
    for category in categories:
        print(">>" + str(category))

        for product in category.products:
            print(product)
