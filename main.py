# This program can hack messages encrypted 
# with the Caesar cipher from the previous project, even 
# if you don’t know the key. There are only 26 
# possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
# this technique a brute-force attack.

import string
import re
import enchant


alphabet = string.ascii_lowercase + string.punctuation + string.digits

# function receives input if user want to encrypt or decrypt

def encrypt_or_decrypt():
    answer = input("Do You want to encrypt (type 'e') or decrypt (type 'd')? \n").lower()
    while answer not in ['e','d']:
        print("You have typed wrong symbol, try again.")
        answer = input("Do You want to encrypt (type 'e') or decrypt (type 'd')?\n")
    return answer

# function checks if key is an integer from 0 to 26

def get_validate_key():
    key_ = input("Please enter the key (0 to 68) to use.\n")
    while not key_.isdigit() or not (0 <= int(key_) <= 68):
        print("You have entered an invalid key. Please enter an integer between 0 and 26.")  
        key_ = input("Please enter the key (0 to 26) to use.\n")
    key_ = int(key_)    
    return key_

# function checks if letters in message only contains characters in alphabet, numbers, and signs


def get_validate_text():
    text = (input("Enter the message.\n")).lower()
    match = re.findall(r"[\sabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789]", text)      
    while len(match) != len(text):
        print("Text must contain latin letters, symbols or numbers.")       
        text = (input("Enter the message to encrypt.\n")).lower()
    return text


# function receives inputs if user want to continue to use a programme or not

def end_dec_again():
    again_answer = input("Do You want to encrypt / decrypt again? (y/n)")  
    while again_answer not in ['y', 'n']:
        print("You have typed wrong symbol, try again (y/n).")
        again_answer = input("Do You want to encrypt / decrypt again? (y/n)")  
    return again_answer


#this function:
# goes through text, checks for spaces and adding spaces to ecrypted text if found
# going through alphabet checking if letters from text is the same as letters in alphabet and symbols, using
# from alphabet if yes then counting new index by adding key to index of letter of alphabet.
# Modulo is clarify that newly found index is in the range of alphabet.

def encrypt(text, key_):
    encrypted_text = ""    
    for i in range(len(text)):        
        if text[i] == ' ':
                encrypted_letter = ' '
                encrypted_text += encrypted_letter
                continue
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                encrypted_letter = alphabet[(j + key_) % len(alphabet)]
                encrypted_text += encrypted_letter
                break
    return encrypted_text  

#checks if decrypted text is semantical

def check_if_words_valid(text):
    compiler = re.compile(r'[a-zA-Z]+')
    text = compiler.findall(text)
    for word in text:  
        vocabulary = enchant.Dict("en_US")
        valid_word = vocabulary.check(word)
        if not valid_word:
            return False
    return True

# take a key in range of 0, 68
# going through text, checking for spaces and adding spaces to text if found
# going through alphabet checking if letters from text is the same as letter
# from alphabet if yes then counting new index by adding key to index of letter of alphabet.
# Modulo is clarify that newly found index is in the range of alphabet.

def decrypt(text):
    decrypted_text = ''
    for key in range(0, 68):
        for i in range(len(text)):       
            if text[i] == ' ':
                decrypted_letter = ' '
                decrypted_text += decrypted_letter
                continue        
            for j in range(len(alphabet)):                
                if text[i] == alphabet[j]:
                    decrypted_letter = alphabet[(j - key) % len(alphabet)]
                    decrypted_text += decrypted_letter                        
                    break
        text_valid = check_if_words_valid(decrypted_text)
        if text_valid:            
            return decrypted_text
        else:
            decrypted_text = ''


#this function runs the programme 

def run_cipher():
    result = ''
    while True:
        answer = encrypt_or_decrypt()
        key_ = get_validate_key()
        text = get_validate_text()        
        if answer == 'e':
            result = encrypt(text, key_)          
        elif answer =='d':
            result = decrypt(text)
        print(result)
        again_answer = end_dec_again()    
        if again_answer =='n':
            break

run_cipher()




    

    
