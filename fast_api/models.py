from database import Base
from sqlalchemy import Column,Integer,String,Boolean

class Book(Base):
    __tablename__ = "Books"
    
    id = Column(Integer,primary_key = True, index = False)
    title = Column(String)
    description = Column(String)
    author = Column(String)
    rating = Column(Integer,default = 0)
    publish_date = Column(Integer)


