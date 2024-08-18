import csv

def get_divisible_numbers(n, results=None):
    if results is None:
        results = []

    if n < 3:
        return results
    
    if n % 3 == 0 ^ n % 5 == 0:
        results.append(n)
    
    return get_divisible_numbers(n-1, results)

print(get_divisible_numbers(100))

'''
Why does the one above not work? please let me know

'''

def get_divisible_numbers(n, results=None):
    if results is None:
        results = []

    if n < 3:
        return results
    
    if (n % 3 == 0 or n % 5 == 0) and not (n % 3 == 0 and n % 5 == 0):
        results.append(n)
    
    return get_divisible_numbers(n-1, results)

print(get_divisible_numbers(100))


def is_word_present(word, words_array):
        for w in words_array:
            if w.lower() == word.lower():
                return True
        return False

def find_words(filename, letter, number):
    found_words = []
    try:
        with open(filename) as file:
            for line in file:
                # print(line, "\n\n\n\n\n")
                for word in line.split():
                    # print(word)
                    # for word in words:
                    if word[0].lower() == letter.lower() and not is_word_present(word, found_words):
                        found_words.append(word)
                        if len(found_words) >= number:
                            return found_words

            while len(found_words) < number:
                found_words.append(None)
            
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return []

    return found_words

def generate_calendar(weekday, num_days):
    num_weeks = (num_days + weekday) // 7 + 1

    calendar = [['  ' for _ in range(7)] for _ in range(num_weeks)]
    day = 1
    for i in range(num_weeks):
        for j in range(7):
            if i == 0 and j < weekday:
                continue
            if day > num_days:
                break
            if day < 10:
                calendar[i][j] = "0" +str(day)
            else:
                calendar[i][j] = str(day)
            day += 1
    
    return calendar

def main():
    
    # print(find_words("./unit-13-LyingScholar/data/atotc.txt","a",5))
    # print(find_words("./unit-13-LyingScholar/data/atotc.txt","d",5))
    # print(find_words("./unit-13-LyingScholar/data/atotc.txt","h",5))
    # print(find_words("./unit-13-LyingScholar/data/atotc.txt","j",5))
    # print(find_words("./unit-13-LyingScholar/data/atotc.txt","t",5))
    # print(find_words("./unit-13-LyingScholar/data/atotc.txt","x",5))
    # print(find_words("./unit-13-LyingScholar/data/atotc.txt","z",5))
    print(get_divisible_numbers(100))
    for line in generate_calendar(2,31):
        print(line)
    
main()