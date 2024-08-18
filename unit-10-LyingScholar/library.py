from cardcatalog import CardCatalog
from book import Book
from patrons import Patron
import csv


class Library:
    def __init__(self,filename):
        self.shelves = []
        self.patrons = [] #collection of patrons
        self.card_catalog = CardCatalog()

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for record in csv_reader:
                title = record[0]
                author = record[1]
                copies = int(record[2])
                book = Book(title, author,copies)
                
                self.shelves.append(book)
                
                if title not in self.card_catalog.lookup_by_title:
                    self.card_catalog.lookup_by_title[title] = []
                    
                self.card_catalog.lookup_by_title[title].append(book)
                
                
                
                if title not in self.card_catalog.lookup_by_author:
                    self.card_catalog.lookup_by_author[author] = []
                    
                self.card_catalog.lookup_by_author[author].append(book)
            
    def search_by_title(self, title):
        if title in self.card_catalog.lookup_by_title:
            return self.card_catalog.lookup_by_title[title]
        else:
            return []

    def search_by_author(self, author):
        if author in self.card_catalog.lookup_by_author:
            return self.card_catalog.lookup_by_author[author]
        else:
            return []
            
    def add_book(self, book):
        self.all_books.append(book)
        
    def checkout(self, book, patron):
        if book.copies > 0 and len(patron.has_books) < 3:
            patron.has_books.append(book)
            book.copies -=1
        else:
            patron.wants_books.append(book)

    def return_book(self, book, patron):
        patron.has_books.remove(book)
        book.copies +=1
        for patron in self.patrons:
            if book in patron.wants_book:
                if len(patron.has_books)<3:
                    patron.has_books.remove(book)
                    patron.wants_books.append(book)
                    book.copies -=1
