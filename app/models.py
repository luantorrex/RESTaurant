from app import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(80))

    def __repr__(self):
        return '<Plate %r>' % self.name