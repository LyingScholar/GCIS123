"""
I'm gonna play Balder's gate till I unlock true Necromancy
"""
import csv

def word_search(filename):
    letter = input("Enter letter :")
    a = 0
    with open(filename) as file:
        # try:
        for csv_reader in csv.reader(file):
            for line in csv_reader:
                for word in line.split():
                    if word.lower()[0] == letter.lower():
                        a+=1
        # except:
        #     return None
    return a

def zip_lookup(zip):
    a = 0
    filename = "unit-13-LyingScholar/data/zip_codes.csv"
    with open(filename) as file:
        checker = 0
        for csv_reader in csv.reader(file):
            for line in csv_reader:
                if line == zip:
                    checker +=1
                elif checker == 1:
                    print(line)
                    checker +=1
                else:
                    continue
    if checker == 0:
        print ("Zipcode not found")

def is_power(a,b):
    if a==1:
        return True
    if a%b==0:
        return is_power(a/b,b)
    else:
        return False
    
def what_power(a,b, count= 0):
    if a==1:
        return count
    if a%b==0:
        return is_power(a/b,b,count+1)
    else:
        raise ValueError(a, " is not a power of ",b)
    
def fill_array(an_array,start=0,step=1,index = 0):
    if index >= len(an_array):
        return
    else:
        an_array[index]=start
        fill_array(an_array,start+step,step,index+1)

def reversal(list):
    output=[]
    index = len(list)-1
    while index>=0:
        output.append(list[index])
        index -=1
    return output

def table(r,c):
    t = []
    for row in range(r):
        t_r = []
        for col in range(c):
            t_r.append((row,col))
        t.append(t_r)
        
    return t

def print_table(t):
    for row in range(len(t)):
        for col in range(len(t[0])):
            print(t[row][col], end = " ")
        print("")
    
def main():
    # print(word_search("unit-13-LyingScholar/data/atotc.txt"))
    zip = input("Enter zip :")
    zip_lookup(zip)
    
    tbl = table(5,5)
    print_table(tbl)

main()