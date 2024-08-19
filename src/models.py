import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    
    def serialize(self):
        return {
            "user_id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
    

class Follower(Base):
    __tablename__ = "Follower"

    user_from_id = Column(Integer, ForeignKey(User.id), primary_key=True, nullable=False)
    user_to_id = Column(Integer, ForeignKey(User.id), primary_key=True, nullable=False)


    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }


class Post(Base):
    __tablename__ = "Post"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)


    def serializ(self):
        return {
            "post_id": self.id,
            "user_id": self.user_id
        }
    

class Media(Base):
    __tablename__ = "Media"

    id = Column(Integer, primary_key=True,)
    type = Column(Enum("photo", "video", "reel"), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey(Post.id), nullable=False)


    def serialize(self):
        return {
            "media_id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }


class Comment(Base):
    __tablename__ = "Comment"

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(450), nullable=False)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)
    post_id = Column(Integer, ForeignKey(Post.id), nullable=False)


    def serialize(self):
        return {
            "comment_id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
