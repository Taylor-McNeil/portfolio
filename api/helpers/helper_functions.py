from api.database import books_collection, counters

def filter_books(title=None, author_firstname=None, author_lastname = None, genre= None ):
    query = {}
    if genre:
        query["genre"] = {"$regex": genre, "$options": "i"}
    if author_firstname:
        query["author_firstname"] = {"$regex": author_firstname, "$options": "i"}
    if author_lastname:
        query["author_lastname"] = {"$regex": author_lastname, "$options": "i"}  
    if title:
        query["title"] = {"$regex": title, "$options": "i"}   
    books_data = list(books_collection.find(query, {"_id": 0}))  # Exclude MongoDB's internal _id field
    books = [Book(**books_data) for book in books_data]

    return books   

def get_next_book_id():
    book_id_count = counters.find_one_and_update(
        {"key":"book_id"},
        {"$inc":{"count":1}},
        return_document=True,
        upsert=True
    )
    return book_id_count["count"]