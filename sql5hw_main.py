import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sql5hw import create_tables, Publisher, Shop, Book, Stock, Sale


DSN = "postgresql://postgres:ab2003@localhost:5432/hw5"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


name = input("Введите имя автора: ")
query = session.query(Stock, Book.title, Shop.name, Sale.price, Sale.date_sale)
query = query.join(Sale)
query = query.join(Shop)
query = query.join(Book)
query = query.join(Publisher)

records = query.filter(Publisher.name == (name))


for c in records:
    print(f' Название книги: {c[1]}, Магазин: {c[2]}, Стоимость: {c[3]}, Дата покупки: {(c[4]).day}-{(c[4]).month}-{(c[4]).year}')

session.close()