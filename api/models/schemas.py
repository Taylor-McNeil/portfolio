from pydantic import BaseModel, Field
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
    book_id:int 
    title: str = Field(min_length=3, max_length=50,description="Title of the book.")
    author_firstname: str = Field (min_length=1, max_length=25, description="Author's first name.")
    author_lastname: str = Field (min_length=1, max_length=25, description="Author's last name.")
    genre: Genre
    summary: str = Field (min_length=1, max_length=500, description="A summary of the book.")    

    class Config:
        json_schema_extra = {
            "examples": [{
                "book_id": 1,
                "title": "Harry Potter and the Sorcerer's Stone",
                "author_firstname": "J.K.",
                "author_lastname": "Rowling",
                "genre": "Fantasy",
                "summary": "A young boy discovers he is a wizard and begins his journey at Hogwarts School of Witchcraft and Wizardry."
            }]
        }

class BookInput(BaseModel):    
    title: str = Field(min_length=3, max_length=50,description="Title of the book.")
    author_firstname: str = Field (min_length=1, max_length=25, description="Author's first name.")
    author_lastname: str = Field (min_length=1, max_length=25, description="Author's last name.")
    genre: Genre
    summary: str = Field (min_length=1, max_length=500, description="A summary of the book.")    

    class Config:
        json_schema_extra = {
            "examples": [{
                "title": "Harry Potter and the Sorcerer's Stone",
                "author_firstname": "J.K.",
                "author_lastname": "Rowling",
                "genre": "Fantasy",
                "summary": "A young boy discovers he is a wizard and begins his journey at Hogwarts School of Witchcraft and Wizardry."
            }]
        }

class ErrorResponse(BaseModel):
    loc: list[str]  # Location of the error, e.g., ["body", "title"]
    msg: str  # Error message, e.g., "Field length validation failed"
    type: str  # Type of validation error, e.g., "value_error.any_str.min_length"

class ValidationErrorResponse(BaseModel):
    detail: list[ErrorResponse]
    error_message: str = "Validation Error"    

class CreateBookResponse(BaseModel):
    message: str
    book: Book    