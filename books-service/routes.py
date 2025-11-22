from flask import Blueprint, jsonify, request
from models import Book
from extensions import db
from services import token_required


book_bp = Blueprint('book', __name__)


@book_bp.route('/books', methods=['POST'])
@token_required
def create_new_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    published_date = data.get('published_date')

    if not title or not author or not published_date:
        return jsonify({"msg": "Missing required fields"}), 400

    new_book = Book(title=title, author=author, published_date=published_date)

    db.session.add(new_book)
    db.session.commit()

    return jsonify({"msg": "Book created successfully", "book_id": new_book.id}), 201


@book_bp.route('/books', methods=['GET'])
@token_required
def list_all_books():
    books = Book.query.all()
    books_list = [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "published_date": book.published_date.isoformat() if book.published_date else None
        }
        for book in books
    ]
    return jsonify(books_list), 200


@book_bp.route('/books/<book_id>', methods=['GET'])
@token_required
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"msg": "Book not found"}), 404

    book_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "published_date": book.published_date.isoformat() if book.published_date else None
    }
    return jsonify(book_data), 200


@book_bp.route('/books/<book_id>', methods=['PUT'])
@token_required
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"msg": "Book not found"}), 404

    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.published_date = data.get('published_date', book.published_date)

    db.session.commit()

    return jsonify({"msg": "Book updated successfully"}), 200


@book_bp.route('/books/<book_id>', methods=['DELETE'])
@token_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"msg": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"msg": "Book deleted successfully"}), 200