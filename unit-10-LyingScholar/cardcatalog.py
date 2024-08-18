
class CardCatalog:
    
    __slots__=["lookup_by_title","lookup_by_author"]
    
    def __init__(self):
        
        self.lookup_by_title = {} #key= title, vlaue= list of books
        self.lookup_by_author = {} #key= author vlaue= list of books
    