def pi_tester():
    pi_cleansed = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    x = 1
    print ("enter digits of pi: ", end = "")
    three = input("")
    if int(three) != 3:
        print("wrong answer, correct answer: 3")
    else:
        while True:
            number_entered = input("enter next digit: ")
            if x == 100:
                print("Yay! you know pi")
                break
            elif number_entered == pi_cleansed[x]:
                x += 1
                continue
            else:
                print("wrong answer, correct answer:", pi_cleansed[x])
                break
    return x
                
def display_score(score):
    if(0 <= score and score <= 4):
        print("PI Neophyte")
    elif(5 <= score and score <= 9):
        print("PI Novice")
    elif(10 <= score and score <= 24):
        print("PI Journeyman")
    elif(25 <= score and score <= 49):
        print("PI Enthusiast")
    elif(50 <= score and score <= 96):
        print("PI Connoisseur")
    elif(96 <= score and score <= 100):
        print("PI Expert")
    else:
        print("PI Imposter")

def main():
    display_score(pi_tester())
    
main()    