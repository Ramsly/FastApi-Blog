from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    f_name = Column(String(50))
    l_name = Column(String(50))
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)

    blogs = relationship('Blog', cascade='')


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(150))
    created_at = Column(DateTime, default=func.now())
    visible = Column(Boolean, default=True)


class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('blogs.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Integer, default=1)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(150), default="")
    created_at = Column(DateTime, default=func.now())


