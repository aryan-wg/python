from database import engine,session_local
import models

from sqlalchemy.orm import Session

from typing import Annotated, Optional
from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel,Field 
from starlette import status


models.Base.metadata.create_all(bind=engine)
def get_db_session():
    db = session_local() 
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session,Depends(get_db_session)]

app = FastAPI()

class BookRequest(BaseModel):
    id:Optional[int] = Field(description="ID not needed",default = None)
    title: str = Field(min_length=3,default = None)
    author: str = Field(min_length=3,default = None)
    description: str = Field(min_length=1, max_length=100,default = None)
    rating: int = Field(gt=0, lt=7,default = None)
    publish_date:int = Field(gt=1400,lt=2200, default=None)

    model_config = {
            "json_schema_extra":{
                "example":{
                    "id":4,
                    "title":"Test book",
                    "author":"Test author",
                    "description":"Test description",
                    "rating":5,
                    "publish_date":3
                    }
                }
            }


class Book:
    id:int
    title: str 
    author: str
    description: str
    rating: int
    publish_date:int
    
    def __init__(self, id, title, author, description, rating, publish_date):
        print(id, title, author, description, rating)
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date

BOOKS = [
    Book(1,"author1", "book1", "desc1", 2,2001),
    Book(2,"author2", "book2", "desc2", 4,2020),
    Book(3,"author3", "book3", "desc3", 1,1990),
    Book(4,"author4", "book4", "desc4", 3,2004),
]


@app.get("/book",status_code = status.HTTP_200_OK)
async def get_with_body_api(db:db_dependency):
    return db.query(models.Book).all()

@app.post("/book",status_code = status.HTTP_201_CREATED)
async def add_book(book_req:BookRequest,db:db_dependency):
    try:
        new_book = models.Book(**book_req.model_dump())
        data = db.add(new_book)
        db.commit()
        return "success" 
    except:
        return "There has been some error"

@app.put("/book",status_code = status.HTTP_200_OK)
async def update_book(book_req:BookRequest,db:db_dependency):
    book = db.query(models.Book).filter(models.Book.id == book_req.id).first()
    try:
        if book:
            book.author = book_req.author
            book.title = book_req.title
            book.description = book_req.description
            book.rating = book_req.rating
            book.publish_date = book_req.publish_date
            
            db.commit()
            return "Success" 
        else:
            raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail = f"No book found with id {book_req.id}")
    except:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,detail = "There has been some error")

    # raise HTTPException(status_code = 404,detail = "Book not found")


@app.patch("/book",status_code = status.HTTP_200_OK)
async def patch_book(book_req:BookRequest,db:db_dependency):
    book = db.query(models.Book).filter(models.Book.id == book_req.id).first()
    try:
        if book:
           updated_data = book_req.dict(exclude_unset = True) 
           for key,value in updated_data.items():
               setattr(book,key,value)
           db.commit()
        else:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"No book found with id {book_req.id}")
    except Exception as e:
        print(e)
        return "There has been an error"


