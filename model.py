""" Models for travel app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__= "users"

    user_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(8))
    first_name = db.Column(db.String)
    last_name = db.Coulmn(db.String)
    email = db.Column(db.String, unique=True)


class Trip(db.Model):
    """A trip."""

    __tablename__= "trips"

    trip_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    trip_name = db.Column(db.String)
    location = db.Column(db.String)
    start_date = db.Column(db.Integer)
    end_date = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey=('users=user_id'))

































































def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///travel'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    