from api.models.schemas import Book

books = [

Book(book_id=1,title="Harry Potter and the Sorcerer's Stone", author_firstname="J.K.", author_lastname="Rowling", genre="Fantasy", summary = "Eleven-year-old Harry discovers he’s a wizard and begins his magical education at Hogwarts, where he encounters friends, foes, and a quest to protect the Sorcerer’s Stone from falling into the wrong hands. In the end, Harry confronts Voldemort, who’s trying to regain power, and stops him for the first time."),
Book(book_id=2,title="Harry Potter and the Chamber of Secrets",  author_firstname="J.K.", author_lastname="Rowling", genre="Fantasy", summary = "Returning to Hogwarts, Harry faces an ancient threat that petrifies students and learns of the Chamber of Secrets, a hidden lair of Salazar Slytherin. With help from his friends, Harry discovers and defeats the creature inside—saving Ginny Weasley and foiling another plot of Voldemort’s."),
Book(book_id=3,title="Harry Potter and the Prisoner of Azkaban", author_firstname="J.K.", author_lastname="Rowling", genre="Fantasy", summary="Harry learns that Sirius Black, a dangerous escaped prisoner, is after him, only to discover that Sirius is actually his godfather and a friend of his parents. The story unveils the betrayal that led to his parents’ death, and with time travel, Harry saves both Sirius and an innocent creature, Buckbeak."),
Book(book_id=4, title="Harry Potter and the Goblet of Fire", author_firstname="J.K.", author_lastname="Rowling",genre="Fantasy", summary="Harry is unexpectedly chosen to compete in the deadly Triwizard Tournament, facing dangerous tasks and ultimately coming face-to-face with Voldemort, who regains his full strength and power. The return of Voldemort changes everything, marking a darker turn for Harry and the wizarding world.")

]