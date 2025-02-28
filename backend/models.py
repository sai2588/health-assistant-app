
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChatLog(Base):
    __tablename__ = 'chat_logs'

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    response = Column(String)
            