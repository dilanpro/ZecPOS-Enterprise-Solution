"""Database Models"""
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from consts import Roles
import hashlib

Base = declarative_base()


class User(Base):
    """User Model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(Integer)

    email = Column(String)
    phone = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow())

    @staticmethod
    def hash(text: str):
        """Hash Text"""
        return hashlib.sha256(text.encode()).hexdigest()

    def check_password(self, password: str):
        """Check Password"""
        return self.password == self.hash(password)


class Domain(Base):
    """Domain Configuration Model"""

    __tablename__ = "domain"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    onboard_admin_id = Column(Integer, ForeignKey("users.id"))


engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db = Session()
