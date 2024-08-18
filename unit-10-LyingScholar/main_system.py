from cardcatalog import CardCatalog
from book import Book
from patrons import Patron
from library import Library
import csv

def main():
    library = Library("unit-10-LyingScholar/data/books.csv")
    
    patron= Patron("000-001","Sam")
    
    library.patrons.append(patron)
    
    print(patron.id, patron.name, patron.wants_books, patron.has_books, len(patron.wants_books),len(patron.has_books))
    
    books = library.search_by_title("The Berlin Stories")
    library.checkout(books[0],patron)
    
    books = library.search_by_title("Atonement")
    library.checkout(books[0],patron)
    
    books = library.search_by_title("Blood Meridian")
    library.checkout(books[0],patron)
    
    books = library.search_by_title("Animal Farm")
    library.checkout(books[0],patron)
    
    print(patron.id, patron.name, patron.wants_books, patron.has_books, len(patron.wants_books),len(patron.has_books))
    



main()