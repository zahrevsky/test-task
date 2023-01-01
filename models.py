import os

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base

db_url = os.environ.get('DB_URL')
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()


class Hall(Base):
    __tablename__ = 'hall'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    street = Column(String)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    hall_id = Column(Integer, ForeignKey('hall.id'))
    coach_id = Column(Integer, ForeignKey('user.id'))
    hall = relationship('Hall', back_populates='lessons')
    coach = relationship('User', back_populates='lessons')

Hall.lessons = relationship('Lesson', order_by=Lesson.id, back_populates='hall')
User.lessons = relationship('Lesson', order_by=Lesson.id, back_populates='coach')
