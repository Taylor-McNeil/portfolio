from pydantic import BaseModel
from enum import Enum

# Genre Enum
class Genre(str, Enum):
    fiction = "Fiction"
    historical_fiction = "Historical Fiction"
    fantasy = "Fantasy"
    science_fiction = "Science Fiction"
    mystery = "Mystery"
    romance = "Romance"

# Book schema
class Book(BaseModel):
    book_id:str
    title: str
    author_firstname: str
    author_lastname: str
    genre: Genre
    summary: str    