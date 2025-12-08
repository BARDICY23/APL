from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
Base = declarative_base()
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"
def setup():
    engine = create_engine('sqlite:///books.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
if __name__ == '__main__':
    s = setup()
    s.add(Book(title='Python Basics', author='Guido'))
    s.add(Book(title='AI with Python', author='Mohamed'))
    s.commit()
    for b in s.query(Book).all():
        print(b)
