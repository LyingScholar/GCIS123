"""
Implement your solution to the practicum in this file.

@author Oscar Capraro
"""
import math
PHONETIC_ALPHABET = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
    "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", 
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", 
    "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
def euclidean_distance(point1,point2):
    i = 0
    a = 0
    if len(point1)==len(point2):
        for i in range(len(point1)):
            a += (point1[i]-point2[i])**2
        return math.sqrt(a)
    else:
        return None
    
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
        19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
        90: 'Ninety', 0: 'Zero'}

def n2w(n):
    if n<100:
        return n2w_less_than_100(n)
    elif n>10000:
        return None
    elif n>=100 and n<1000:
        return str(num2words[n//100])+ ' hundred ' + str((n2w_less_than_100(n-(n//100))).lower)
    elif n>=1000 and n<10000:
        return str(num2words[n//1000])+ 'thousand' + str((n2w_less_than_100(n-(n//100))).lower)

def n2w2(n):
    return n2w_less_than_100(int(str(n)[0]))

def n2w_less_than_100(n):
    try:
        return (num2words[n])
    except KeyError:
        try:
            return (num2words[n-n%10] + ' '+ num2words[n%10].lower())
        except KeyError:
            return 'Errorer'

def get_length_and_value(item):
        return (10000-len(str(item)), item)
    # lol

def get_first_digit(item):
        return str(item)[0]
    
def freq_sorted(lst):
    if len(lst)<1:
        return []
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

    sorted_list = sorted(frequency_dict, key=(frequency_dict.get), reverse = True)
    result = []
    for item in sorted_list:
        result.extend([item] * frequency_dict[item])
    return result

def data_sorter(lst):
    sorted_first_digit_1 = sorted(lst, key=n2w2)
    sorted_first_digit_2 = sorted(lst, key=n2w)
    sorted_dig_then_val = sorted(lst,key=get_length_and_value)
    
    frequency_sorted = freq_sorted(lst)
    
    return sorted_first_digit_1, sorted_dig_then_val,frequency_sorted

def phonetic_translation(lst):
    words = lst.split()
    code = []
    for word in words:
        for i in word:
            try:
                adder = PHONETIC_ALPHABET[ord(i.lower())-97]
                code.append(adder)
            except:
                continue
    return code
    
def words_by_letter(list):
    words = list.split()
    words_by_first_letter = {}

    for word in words:
        first_letter = word[0].lower()
        if first_letter not in words_by_first_letter:
            words_by_first_letter[first_letter] = set()
        words_by_first_letter[first_letter].add(word.lower())
    return words_by_first_letter
def main():
    data = [10,3000,5,20,10,3,100,3000,3120,100]
    print(freq_sorted(data))
    # you may use this function to manually test your code if you feel the need
    # to do so.
    return

if __name__ == "__main__":
    main()