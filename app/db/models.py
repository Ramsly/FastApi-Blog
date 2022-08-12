from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String)
    f_name = Column(String(50), default="")
    l_name = Column(String(50), default="")
    disabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)

    blogs = relationship('Blog')


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(50))
    content = Column(String(150))
    created_at = Column(DateTime, default=func.now())
    visible = Column(Boolean, default=True)

    comments = relationship('Comment')
    likes = relationship('Like')


class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('blogs.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Integer, default=1)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('blogs.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(150), default="")
    created_at = Column(DateTime, default=func.now())


