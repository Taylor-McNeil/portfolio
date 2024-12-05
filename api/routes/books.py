from fastapi import APIRouter, HTTPException, Query, Path, status
from api.models.schemas import Book, BookInput, CreateBookResponse
from api.helpers.error_responses import generate_422_response
from api.database import books_collection
#from api.data.data import books
from api.helpers.helper_functions import filter_books, get_next_book_id
from typing import Optional



router = APIRouter()

@router.get(
        "/books/{book_id}",
          response_model=Book, 
          summary="Retrieve Book Details by Book ID",
          responses= generate_422_response("book_id")
          )

def get_book(book_id: int = Path(...,description="A unique identifier for a book.")):
    """
    Retrieve details of a `Book` by its `book_id`.

    ### Parameters:
    - **`book_id`** *(int)*: The unique ID of the book. Must be a positive integer.

    ### Returns:
    - **`Book` object**: The details of the requested book.

    ### Raises:
    - **HTTPException 404**: No book with the given `book_id` exists.
    - **HTTPException 400**: `book_id` is invalid. Must be a postive integer.
    - **HTTPException 500**: No books in the database.
    """
    #Validate the input
    if book_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid book ID. Book ID must be a positive integer."
        )
    # TODO: Create an edge case for no books in the collection. If database gets flushed.
    if books_collection.count_documents({}) == 0:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="There are no books in the database. Please add a book."
        )

    book = books_collection.find_one({"book_id": book_id},{"_id":0})
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with book ID: {book_id} not found."
        )
    

    return book

@router.get(
        "/books", 
        response_model=list[Book], 
        summary="Retrieve a List of Books",
        responses= generate_422_response("title","author_firstname","author_lastname","genre")
          )

def list_books(
    title: Optional[str]=Query(None, min_length=3, max_length=50, description="Filter books by title."),
    author_firstname: Optional[str]=Query(None, min_length=3, max_length=25, description="Filter books by author's first name."), 
    author_lastname:Optional[str]=Query(None, min_length=3, max_length=25, description="Filter books by author's last name."),
    genre: Optional[str]=Query(None,min_length=3, max_length=25, description="Filter books by genre.")
         ):

    """
        Retrieve a list of `Books` based on a list of optional criteria.

        ### Parameters:
         - **title** *(str, optional)*: The name of the book.
         - **author_firstname** *(str, optional)*: The first name of the book's author.
         - **author_lastname** *(str, optional)*: The last name of the book's author.
         - **genre** *(str, optional)*: The genre of the book. 
            - Possible options:
                - "Fiction"
                - "Historical Fiction"
                - "Fantasy"
                - "Science Fiction"
                - "Mystery"
                - "Romance"

        ### Returns:
        - list[Book]: A list of books matching the provided filters.
        - An empty list of no books match the criteria.

        ### Raises:
        - **HTTPException 422**: Occurs if any parameter fails validation (e.g., invalid length or type).

    """
    return filter_books(title,author_firstname,author_lastname,genre)

@router.post(
        "/books", 
        summary="Create a New Book", 
        response_model=CreateBookResponse, 
        responses=generate_422_response("title","author_firstname","author_lastname","genre","summary")
            )

def create_book(book: BookInput):
   
    """
    Create a new book from user-provided data.

    ### Parameters:
    - **book** *(BookInput)*: A JSON object containing the book's details, provided in the request body. 
    
        - Expected Fields:
            - `title` *(str)*: The title of the book.
            - `author_firstname` *(str)*: The first name of the book's author.
            - `author_lastname` *(str)*: The last name of the book's author.
            - `genre` *(str)*: The genre of the book. Must be one of the predefined options.
            - `summary` *(str)*: A brief summary of the book.
    
   
    ### Notes
    - The `genre` must be one of the predefined options:
        - Fiction
        - Mystery
        - Historical Fiction
        - Fantasy
        - Science Fiction
        - Romance  
   
    ### Returns
    - **dict**: A dictionary containing a success message and the details of the created book. The created book follows the `book` schema.
     
    ### Raises
    -  **HTTPException 422**: If the input data (e.g., genre or other fields) fails validation.
    
    """
   
    try:
        book_id = get_next_book_id()

        new_book = {
            "book_id": book_id,
            "title": book.title,
            "author_firstname" : book.author_firstname,
            "author_lastname" : book.author_lastname,
            "genre": book.genre,
            "summary": book.summary
            }
        
        result = books_collection.insert_one(new_book)

        new_book["_id"] = str(result.inserted_id)

        return {"message": "Book created successfully", "book": new_book}

    except Exception as e:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred: {str(e)}"
        )






