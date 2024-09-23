from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

# BOOKS = [
#     {"id": 1, "title": "book1", "description": "desc1", "rating": 2},
#     {"id": 2, "title": "book2", "description": "desc2", "rating": 3},
#     {"id": 3, "title": "book3", "description": "desc3", "rating": 2},
#     {"id": 4, "title": "book4", "description": "desc4", "rating": 5},
#     {"id": 5, "title": "book5", "description": "desc5", "rating": 1},
# ]


class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=7)


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        print(id, title, author, description, rating)
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1,"author1", "book1", "desc1", 2),
    Book(2,"author2", "book2", "desc2", 4),
    Book(3,"author3", "book3", "desc3", 1),
    Book(4,"author4", "book4", "desc4", 3),
]


@app.get("/")
async def init_books():
    return BOOKS

@app.post("/add")
async def add_book(book_req:BookRequest):
    print("hellooo")
    new_book = Book(**book_req.model_dump())
    print(new_book)
    BOOKS.append(new_book)
    return BOOKS

@app.get("/body")
async def get_with_body_api(data=Body()):
    print(data)
    return {"message": "Hello world"}


@app.post("/body")
async def post_with_body_api(data=Body()):
    print(data)
    return {"message": "Hello world"}
