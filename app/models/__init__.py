"""Models for the Database"""
from enum import unique
from os import name
import flask_login
from ..extensions.sql import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(flask_login.UserMixin, db.Model):
    """User Model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # Credentials
    username = db.Column(db.String(50), unique=True)
    __password = db.Column('password', db.String(256))

    # General Info
    name = db.Column(db.String(100))

    # Permissions
    access_super_admin = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f'<User {self.email}>'

    def set_password(self, password: str) -> None:
        """Set the password for the user."""
        self.__password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.__password, password)
