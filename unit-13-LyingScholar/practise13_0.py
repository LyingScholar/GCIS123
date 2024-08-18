def pig_latin_translator(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[0] in vowels:
            return word + 'ay'
        elif word[i] in vowels:
            word =  word[i:]+word[:i]
            i = 100000000000000000000000000000000000000000000000
    return word + 'ay'
    
    
def ascii_conversions(input_string):
    tokens = input_string.split()
    conversion_type = tokens[0]

    if conversion_type == "i":
        codes = [int(code) for code in tokens[1:]]
        for code in codes:
            character = chr(code)
            print(code,":",character)
    elif conversion_type == "c":
        characters = tokens[1:]
        for character in characters:
            code = ord(character)
            print(code,":",character)
    else:
        print("Invalid input")

def main():
    # word = input("What's your word? ")
    # translated_word = pig_latin_translator(word)
    # print(translated_word)
    ascii_conversions("i 67 97 84")
    
    ascii_conversions("c d O g")
    
main()