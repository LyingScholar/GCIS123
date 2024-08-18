def is_alphabet(letter):
    ascii_value = ord(letter)
    return ascii_value >= 65 and ascii_value <= 90


def encrypt_letter(letter,shift):
    if is_alphabet(letter) == True:
        ascii_value = ord(letter)
        shift = ascii_value + shift
        return chr(shift)
    else:
        return ""

def decrypt_letter(letter,shift):
        ascii_value = ord(letter)
        shift = ascii_value - shift
        decrypted = chr(shift)
        if is_alphabet(decrypted) == True:
            return decrypted
        else:
            return ""

def encrypt_message(message,shift):
    ciphertext= ""
    
    # letter = encrypt_letter(message[0],shift)
    # ciphertext = ciphertext + letter
    
    # letter = encrypt_letter(message[1],shift)
    # ciphertext = ciphertext + letter
    
    # letter = encrypt_letter(message[2],shift)
    for index in message:
        letter = encrypt_letter(index,shift)
        ciphertext = ciphertext + letter

    return ciphertext

def decrypt_message(message):
    index = 0
    ciphertext = ""
    shift = 3
    # while index < len(message):
    #     letter = decrypt_letter(message[index],shift)
    #     ciphertext = ciphertext+letter
    #     index +=1
    for index in message:
        letter = decrypt_letter(index,shift)
        ciphertext = ciphertext + letter

    return ciphertext
    return ciphertext
    
def main():
    print("encrypt:",encrypt_message("XYZ",3))
    print("decrypt:", decrypt_message("[\]"))
    #print(encrypt_letter("A",3))

if __name__ == "__main__":
    main()