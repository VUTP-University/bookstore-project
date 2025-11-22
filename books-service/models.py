import uuid
from extensions import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.String(256), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    
    
    def __init__(self, title, author, published_date):
        self.title = title
        self.author = author
        self.published_date = published_date

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'
    
    
# book_1 = Book(author="George Orwell", title="1984", published_date="1949-06-08")
# book_2 = Book(author="Harper Lee", title="To Kill a Mockingbird", published_date="1960-07-11")