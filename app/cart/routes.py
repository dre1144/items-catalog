from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from app.cart.models import Cart
from app.auth.models import User
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required

@main.route('book/add_to_cart/<book_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(user_id, book_id):
    user_id = User.query.get(user_id)
    prod_id = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.add(Cart.user_id, Cart.prod_id)
        db.session.commit()
        flash('Book added to Cart')
        return redirect(url_for('main.display_books'))
    return render_template('add_to_cart.html', user_id=user_id, prod_id=prod_id)

@main.route('/cart/<user_id>')
@login_required
def display_cart(user_id):
    user = User.query.filter_by(id=user_id).first()
    user_books = Book.query.filter_by(Cart.user_id).all()

    return render_template('cart.html', user=user, user_books=user_books)


