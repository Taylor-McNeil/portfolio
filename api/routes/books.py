from fastapi import APIRouter, HTTPException, Query, status
from api.models.schemas import Book, CreateBook
from api.data.data import books
from typing import Optional

router = APIRouter()

@router.get("/books/{book_id}", response_model=Book, summary="Retrieve Book Details",)
def get_book(book_id: str):
    """
    This endpoint searchers for a book in the collection by its `book_id`.
    If the book is found, it returns the book's details. If not, an HTTP 404
    error is raised with more information.

    """

    for book in books:
        if book.book_id == book_id:
            return book
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Book with book id: {book_id} not found")  

@router.get("/books", response_model=list[Book], summary="Retrieve a List of Books")
def list_books(
    genre: Optional[str]=Query(None,min_length=3, max_length=25, description="Filter books by genre"), 
    author_firstname: Optional[str]=Query(None, min_length=3, max_length=25, description="Filter books by author's first name"), 
    author_lastname:Optional[str]=Query(None, min_length=3, max_length=25, description="Filter books by author's last name")
    ):

    """
    This endpoint returns a collection of books. You can filter the results
    by providing query parameters such as `genre`, `author_firstname`, and/or
    `author_lastname`. If no filters are provided, all books in the collection
    are returned.
    """

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

@router.post("/books", summary="Create a New Book")
def create_book(book: CreateBook):
   """
   Create a new book entry in the system. This endpoint accepts a JSON payload containing details about the book such as the `title`, `summary`, `author_firstname`, `author_last name` and `genre`.
   A unique `book_id` is automatically assigned to the book upon creation.
   
   ### Request Body
    - **title**: (string, required) The title of the book.
    - **author_firstname**: (string, required) The author's name.
    - **author_lastname**: (string, required) The genre of the book.
    - **genre**: (string, required) The year the book was published.
    - **summary**: (string, required) A summary of the book.

    ### Response
    - **message**: A confirmation message indicating the book was created successfully.
    - **book**: The created book object, including its assigned `book_id`.

   """
   book_id = len(books) + 1
   
   new_book = Book(
       book_id= book_id,
       title= book.title,
       author_firstname= book.author_firstname,
       author_lastname= book.author_lastname,
       genre= book.genre,
       summary= book.summary


   )


   books.append(new_book)
   return {"message": "Book created successfully", "book": new_book}
