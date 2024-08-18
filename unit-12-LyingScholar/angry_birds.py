import csv
import random
from list_stack import Stack

class task:
    __slots__= "__name__", "location"
    
    def __init__(self, name, location):
        self.__name__= name
        self.location=location
    
    def print_details(self):
        print("Task Name:",self.__name__)
        print("Task Location=",self.location)
    
    def __str__(self):
        return str(self.__name__) + " in " + str(self.location)
    
    def __repr__(self):
        return str(self.__name__) + " in " + str(self.location)
    

def tasks_creation():
    list_of_tasks = []
    with open("unit-12-LyingScholar/tasks_01.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        for line in csv_reader:
            # print(line)
            name = line[0].strip()
            local = line[1].strip()
            list_of_tasks.append(task(name, local))
        
        # print(list_of_tasks)
        return list_of_tasks

colors = "Black, Blue, Brown, Cyan, Green, Pink, Purple, Red, White, Yellow"

class crewmate:
    __slots__ = "__color__", "assigned_tasks", "__murdered__", "__imposter__", "__all_done__", "location"
    
    def __init__(self, color):
        self.__color__ = color
        self.assigned_tasks= Stack()
        self.location = "cafetaria"
        self.__murdered__= False
        self.__imposter__ = False
        self.__all_done__ = False
        
        
    def print_details(self):
        if not self.__imposter__:
            print("Crewmate:")
            print("color=",self.__color__)
            print("murdered=", self.__murdered__)
            print("tasks:", self.assigned_tasks)
        
    def __str__(self):
        if self.__murdered__:
            return str(self.__color__) + " Crewmate (deceased)"
        return str(self.__color__) + " Crewmate"
    
    def __repr__(self):
        if self.__murdered__:
            return str(self.__color__) + " Crewmate (deceased)"
        return str(self.__color__) + " Crewmate"
    
    def add_task(self, task):
        self.assigned_tasks.push(task)
        
    def done_task(self):
        if self.assigned_tasks.__len__() == 0:
            raise IndexError("no tasks")
        if self.assigned_tasks.__len__() == 1:
            self.__all_done__ = True
            # if stack.__len__ exists why do we need stack.__isEmpty__?
        return self.assigned_tasks.pop()
    
    def set_imposter(self):
        self.__imposter__ = True
    
    def kill(self):
        self.__murdered__=True


class Ship:
    __slots__ = "__n__", "__all_tasks__", "__crew__", "__locations__", "graveyard", "counter"
    
    def __init__(self, imposters):
        self.__n__ = imposters
        self.__all_tasks__= tasks_creation()
        self.__crew__ = {}
        self.graveyard = []
        self.counter = 1
        
        
        colors_list = []
        for color in colors.split(","):
            self.__crew__[color.strip()] = crewmate(color.strip())
            colors_list.append(color.strip())
            number_of_tasks = random.randint(3,6)
            for _ in range(number_of_tasks):
                self.__crew__[color.strip()].add_task(self.__all_tasks__[random.randrange(len(self.__all_tasks__))])
                # I make a set so that i get n different numbers between 1 and 10, then i map it to the colors list
        
        # print(crew)
        random_set = set()
        while len(random_set) < self.__n__:
            random_set.add(int(random.randint(1,10)))#len(colors)
        # print(colors_list)
        for i in random_set:
            # print(crew)
            self.__crew__[colors_list[i-1]].set_imposter()

        locations = set()
        for i in self.__all_tasks__:
            locations.add(str(i.location))
        self.__locations__ = list(locations)
        
    def play_round(self):
        imposter_locations = set()
        self.counter = 0
        for i in range(self.__n__):
            imposter_locations.add(self.__locations__[random.randrange(len(self.__locations__))])
        for crewmate in self.__crew__:
            if not self.__crew__[crewmate].__imposter__:
                if not self.__crew__[crewmate].__all_done__:
                    if not self.__crew__[crewmate].__murdered__:
                        task = self.__crew__[crewmate].done_task()
                        print(str(crewmate) + " begins " + str(task))
                        self.counter += 1
                        if task.location in imposter_locations:
                            self.__crew__[crewmate].kill()
                            self.graveyard.append(self.__crew__[crewmate])
                            print("\tOh no! An imposter is waiting in ambush!",self.__crew__[crewmate]," is murdered!")
                        else:
                            print("Task complete!")
                            print(self.__crew__[crewmate]," heads back to the cafeteria.")
        
    def play_game(self):
        while self.counter !=0:
            self.play_round()
        if len(self.graveyard) + self.__n__ < 10:
            print("The crew made it!")
        else:
            print("The imposters wiped out the crew!")
        results = []
        
        for i in self.__crew__:
            if not self.__crew__[i].__imposter__:
                results.append(self.__crew__[i])
        results.sort(key = death)
        for i in results:
            print(i)
            # i. print_details()

def death(crewmate_object):
    if crewmate_object.__murdered__:
        return True
    return False
    
def main():
    while True:
        try:
            n = int(input("Enter number of imposters: "))
            if int(n) < 5 and int(n) >0:
                break
            else:
                print("Enter a number between 1 and 4")
                continue
        except:
            raise ValueError
    journey = Ship(n)
    journey.play_game()
    
main()