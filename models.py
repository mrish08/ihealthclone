from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()

class User(UserMixin, db.Model):

    """Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "users_user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False, unique=False)
    middlename = db.Column(db.String(255), nullable=True, unique=False)
    lastname = db.Column(db.String(255), nullable=False, unique=False)
    account_type = db.Column(db.String(255), default="Client", blank=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(
        db.String(255), primary_key=False, unique=False, nullable=False
    )
    date_joined = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    updated_at = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.username)
