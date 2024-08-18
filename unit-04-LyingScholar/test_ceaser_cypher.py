import ceaser_cypher

def test_encrypt_letter_g():
    #setup  
    plaintext = "G"
    shift = 5
    expected = "L"
    #invoke
    actual = ceaser_cypher.encrypt_letter("G",5)

    #analyze
    assert actual == expected

def test_encrypt_letter_invalid5():
    #setup  
    plaintext = "5"
    shift = 5
    expected = ""
    #invoke
    actual = ceaser_cypher.encrypt_letter("5",5)

    #analyze
    assert actual == expected

def test_encrypt_letter_star():
    #setup  
    plaintext = "*"
    shift = 5
    expected = ""
    #invoke
    actual = ceaser_cypher.encrypt_letter("*",5)

    #analyze
    assert actual == expected

def test_is_alphabet_a():
    letter = "a"
    expected = False
    
    actual = ceaser_cypher.is_alphabet(letter)
    
def test_decrypt_letter_g():
    #setup  
    plaintext = "L"
    shift = 5
    expected = "G"
    #invoke
    actual = ceaser_cypher.decrypt_letter("L",5)

    #analyze
    assert actual == expected
    
def test_encrypt_message_g():
    #setup  
    plaintext = "HELLO"
    shift = 3
    expected = "KHOOR"
    #invoke
    actual = ceaser_cypher.encrypt_message("HELLO",3)

    #analyze
    assert actual == expected
    
    