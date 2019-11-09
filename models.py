from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone =  db.Column(db.String(14), nullable=False)
    username = db.Column(db.String(14), nullable=False)
    password = db.Column(db.String(14), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False)
    register_date = db.Column(db.DateTime)


class Movers(db.Model):
    __tablename__ = "movers"
    comp_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    company_address = db.Column(db.String(100), nullable=False)
    company_email = db.Column(db.String(100), nullable=False)
    contact =  db.Column(db.String(14), nullable=False)
    logo = db.Column(db.String(150))
    owner = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    num_of_reviews = db.Column(db.Integer)
    business_num = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("location.location_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)



class Bookings(db.Model):
    __tablename__ = "bookings"
    b_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    company_booked =  db.Column(db.String(14), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    moving_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    destination = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("movers.comp_id"), nullable=False)
    moving_id = db.Column(db.Integer, db.ForeignKey("move.mt_id"), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("location.location_id"), nullable=False)




class Reviews(db.Model):
    __tablename__ = "reviews"
    reviews_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    reviewed_comp = db.Column(db.String(100), nullable=False)
    reviewer = db.Column(db.DateTime, nullable=False)
    review_date =  db.Column(db.DateTime, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("movers.comp_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

  
class Roles(db.Model):
    __tablename__ = "roles"
    role_id = db.Column(db.Integer, primary_key=True)
    role_type = db.Column(db.String, nullable=False)


class Location(db.Model):
    __tablename__ = "location"
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(100), nullable=False)


class Move(db.Model):
    __tablename__ = "move"
    mt_id = db.Column(db.Integer, primary_key=True)
    moving_type = db.Column(db.String(100), nullable=False)