
class Patron:
    __slots__ = ["self", "id", "name", "has_books","wants_books"]
    
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.has_books = []
        self.wants_books = []
