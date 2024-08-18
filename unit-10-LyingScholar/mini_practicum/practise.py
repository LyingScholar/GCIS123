def make_letter_frequency(filename):
    letter_count = {}
    with open(filename, 'r') as file:
        text = file.read().lower()
        for char in text:
            if ord(char) >= 97 and ord(char) <= 122:
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1
            # else:
                # print("non-letter found")
    return letter_count

def print_letter_frequency(letter_count):
    max_frequency = 0
    most_popular_letter = ''
    for letter in letter_count:
        print(letter,": ", letter_count[letter])
        if letter_count[letter] > max_frequency:
            max_frequency = letter_count[letter]
            most_popular_letter = letter
    print(f"The most popular letter is '{most_popular_letter}' with a frequency of {max_frequency}")

def main():
    # filename = 'data/rit_mission.txt'
    filename = 'data/alice.txt'
    freq_dict = make_letter_frequency(filename)
    print_letter_frequency(freq_dict)

if __name__ == "__main__":
    main()