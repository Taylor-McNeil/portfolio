def filter_books(books, title=None, author_firstname=None, author_lastname = None, genre= None ):
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