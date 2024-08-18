def gcd(a, b):  # greatest common divisor
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

class Fraction:
    # __slots__ = 'whole', 'numerator', 'denominator'

    def __init__(self,w=0,n=0,d=1):
        self.whole = w
        self.numerator = n
        self.denominator = d

    def get_fraction(self):
        try:
            return (self.whole, self.numerator, self.denominator)
        except:
            return self
    
    # def __repr__(self):
    #     return (self.whole, self.numerator, self.denominator)
    
    def __hash__(self):
        return hash((self.whole, self.numerator, self.denominator))
    
    def simplify(self):
        if self.denominator == 0:
            print("crash")
            raise ZeroDivisionError
        if self.denominator < 0:
            self.denominator = self.denominator * (-1)
            self.numerator = self.numerator * (-1)
        if self.numerator > self.denominator or (self.numerator * (-1)) > self.denominator:
            self.whole += self.numerator//self.denominator
            self.numerator = self.numerator%self.denominator
        if self.numerator < 0:
            self.numerator = self.denominator + self.numerator
            self.whole -= 1
        g = gcd(self.numerator,self.denominator)
        if self.numerator == 0:
            self.denominator = 1
        elif g > 1:
            self.numerator = int(self.numerator/g)
            self.denominator = int(self.denominator/g)
        # if (self.numerator * (-1)) > self.denominator:
        return self
    
    def add(self,input_fraction):
        self.numerator = (self.numerator *input_fraction.denominator) + (self.denominator*input_fraction.numerator)
        self.denominator = self.denominator*input_fraction.denominator
        self.whole += input_fraction.whole
        
        return self
    
    def subtract(self,input_fraction):
        self.numerator = (self.numerator *input_fraction.denominator) - (self.denominator*input_fraction.numerator)
        self.denominator = self.denominator*input_fraction.denominator
        self.whole -= input_fraction.whole
        
        return self
    
    def multiply(self,other):
        up1 = ((self.whole * self.denominator) + self.numerator)
        up2 = ((other.whole * other.denominator) + other.numerator)
        self.numerator = up1*up2
        self.denominator = self.denominator * other.denominator
        self.whole = 0
        return self
    
    # def divide(self,other):
    #     # up1 = ((self.whole * self.denominator) + self.numerator)
    #     # up2 = ((other.whole * other.denominator) + other.numerator)
    #     # self.numerator = up1*(other.denominator)
    #     # self.denominator = self.denominator * up2
    #     # self.whole = 0
    #     # return self.simplify()
    
    #     numerator1 = self.numerator + self.whole * self.denominator
    #     numerator2 = other.numerator + other.whole * other.denominator

    #     new_numerator = numerator1 * other.denominator
    #     new_denominator = numerator2 * self.denominator

    #     return Fraction(0, new_numerator, new_denominator).simplify()
    
    def __str__(self):
        return str(self.whole) + ", " + str(self.numerator) +", " + str(self.denominator)
    
    def divide(self, other):
        numerator1 = self.numerator + self.whole * self.denominator
        numerator2 = other.numerator + other.whole * other.denominator
        denominator = self.denominator * other.denominator

        new_numerator = numerator1 * other.denominator
        new_denominator = numerator2 * self.denominator
        new_fraction = Fraction(0, new_numerator, new_denominator)
        
        return new_fraction.simplify()
        
    def __eq__(self,other):
        if type(self) != type(other):
            return False
        if self.simplify().get_fraction() == other.simplify().get_fraction():
            return True
        return False
        
    def __lt__(self,other):
        if type(self) != type(other):
            return False
        return self.simplify().get_fraction() < other.simplify().get_fraction()
    def __le__(self,other):
        if type(self) != type(other):
            return False
        return self.simplify().get_fraction() <= other.simplify().get_fraction()
    def __gt__(self,other):
        if type(self) != type(other):
            return False
        return self.simplify().get_fraction() > other.simplify().get_fraction()
    def __ge__(self,other):
        if type(self) != type(other):
            return False
        return self.simplify().get_fraction() >= other.simplify().get_fraction()


# print(Fraction(5, 4, 3).simplify())
# # (6, 1, 3)
# print(Fraction(0, 15, -3).simplify())
# # (-5, 0, 1)
# print(Fraction(-7, -6, -4).simplify())
# # (-6, 1, 2)

# sum = Fraction(3,1,2).add(Fraction(2,3,4))
# print(sum)
# print(Fraction(3,1,2))
# # (6, 1, 4)
# print(Fraction(3, 5, -2))
# print(Fraction(1, 2, 3).simplify())
# print(Fraction(0, 10, 6).simplify())

def get_sort_key(f):
    return f.get_fraction()

def unique_sorted_list(fractions):
    
    
    unique_fractions_list = []
    for i in fractions:
        if i.simplify() not in unique_fractions_list:
            unique_fractions_list.append(i.simplify())
    
    unique_fractions_list.sort(key=get_sort_key)
    return unique_fractions_list


def partition(fractions):
    partitions = {}
    for fraction in fractions:
        key = fraction.simplify() #had to do this
        if key not in partitions:
            partitions[key] = []
        partitions[key].append(fraction)
    # partitions_list = list(partitions)
    # return partitions_list
    return partitions

def find_all(partitions, fraction):
    key = fraction.simplify()
    if key in partitions:
        return partitions[key]
    else:
        return []