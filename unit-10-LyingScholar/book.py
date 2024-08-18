class Book:
    __slots__ = ["title", "author","copies"]
    def __init__(self, title, author,copies):
        self.title = title
        self.author = author
        self.copies = copies
