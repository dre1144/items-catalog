from app import db


class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    prod_id = db.Column(db.Integer, db.ForeignKey('book.id'))

def __init__(self, user_id, prod_id):
    self.user_id = user_id,
    self.prod_id = prod_id
