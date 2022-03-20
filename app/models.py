from . import db

class Properties(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(700))
    num_rooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    prop_type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo_name = db.Column(db.String(80))

    def __init__(self, title, description, num_rooms, num_bathrooms, price, prop_type, location, photo_name):
        self.title = title
        self.description = description
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price = price
        self.prop_type = prop_type
        self.location = location
        self.photo_name = photo_name