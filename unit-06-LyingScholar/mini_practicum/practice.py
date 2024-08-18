import csv
import re

def find_rabbit():
    count = 0
    with open("./unit-06-LyingScholar/mini_practicum/alice.txt") as file:    
        for line in file:
            for word in line.split():
                if word == "Rabbit":
                    count += 1
                else:
                    continue    
    return count
    ####Your code goes here

    return count

def find_rabbit_regex ():
    count = 0
    with open("./unit-06-LyingScholar/mini_practicum/alice.txt") as file:    
          for line in file:
            matches = re.findall('Rabbit', line)
            count += len(matches)
    return count
    ####Your code goes here

def main ():
    print ("Found Rabbit", find_rabbit (), "times.") #should be 29
    print ("Found Rabbit", find_rabbit_regex (), "times.") #should be 45
    

if __name__ == "__main__":
    main ()