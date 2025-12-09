from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

book1 = Book(title='Python Basics', author='Guido')
book2 = Book(title='AI with Python', author='Mohamed')
session.add(book1)
session.add(book2)
session.commit()

for book in session.query(Book).all():
    print(f"Book (id={book.id}, title='{book.title}', author='{book.author}')")

session.close()
