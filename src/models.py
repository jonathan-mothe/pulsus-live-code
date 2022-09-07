from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devices.db'
db = SQLAlchemy(app)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    def __repr__(self):
        return f'Localização("{self.lat}", "{self.long}")'


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_lat = db.Column(db.ForeignKey('location.id'), nullable=False)
    location_long = db.Column(db.ForeignKey('location.id'), nullable=False)
    location_lat_id = db.relationship('Location', foreign_keys=[location_lat])
    location_long_id = db.relationship('Location', foreign_keys=[location_long])

    def to_json(self):
        return {"id": self.id, "lat": self.location_lat, "long": self.location_long}
