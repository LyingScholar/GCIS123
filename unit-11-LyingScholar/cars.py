class Car:

    __slots__ = ["__vin", "__make", "__model", "__year","__mileage","__fuel"]

    def __init__(self,vin,make,model,year):
        self.__vin =vin
        self.__make =make
        self.__model =model
        self.__year =year
        self.__mileage = 0
        self.__fuel=0
        
    def print_car(self):
        print("vin: ",self.__vin,"\nmake: ",self.__make,"\nmodel: ",self.__model,"\nyear: ",self.__year,"\nMileage: ",self.__mileage ,"\nFuel: ",self.__fuel)
    
    def filler_up(self,gallons):
        if gallons > 0:
            self.__fuel += gallons
        if gallons >15:
            self.__fuel = 15
    
    def drive(self, miles):
        max_miles = self.__fuel * 30
        if miles > max_miles:
            miles = max_miles
        
        self.__mileage += miles
        self.__fuel -+ miles/30
        

    def __str__(self):
        return "STRING OUTPUT: Vin: "+str(self.__vin)+" Make: "+self.__make + ", Model: " + self.__model

    def __repr__(self):
        return "REPR OUTPUT: Vin: " + str(self.__vin) + " Make: "+ self.__make + ", Model: " + self.__model
    
    def __eq__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin == other.__vin
        
    def __lt__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin < other.__vin
    def __le__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin <= other.__vin
        
    def __gt__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin > other.__vin
        
    def __ge__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin >= other.__vin
        