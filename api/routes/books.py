from fastapi import APIRouter, HTTPException, Query, status
from api.models.schemas import Book
from api.data.data import books
from typing import Optional

router = APIRouter()

# Retrieve book via book id
@router.get("/books/{book_id}", response_model=Book)
def get_book(book_id: str):
    for book in books:
        if book.book_id == book_id:
            return book
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Book with book id: {book_id} not found")  

# Retrieve all books, filtered by genre or author first name or author last name
@router.get("/books", response_model=list[Book])
def list_books(genre: Optional[str]=Query(None), author_firstname: Optional[str]=Query(None), author_lastname:Optional[str]=Query(None)):
    filtered_books = books
    if genre:
         genre= genre.title()
         filtered_books = [book for book in filtered_books if book.genre == genre]
    if author_firstname:
         author_firstname= author_firstname.title()
         filtered_books = [book for book in filtered_books if book.author_firstname== author_firstname]    
    if author_lastname:
        author_lastname = author_lastname.title()
        filtered_books = [book for book in filtered_books if book.author_lastname== author_lastname] 
    return filtered_books

# Create a book
#@router.post("/books")