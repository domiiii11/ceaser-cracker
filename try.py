import re

text = 'I have 9 cats'.lower()





import string

alphabet = string.ascii_lowercase + string.punctuation + string.digits
print(alphabet)

import re


def get_validate_text():
    text = (input("Enter the message.\n")).lower()      
    if set(text) <= set(alphabet):
        print("True")

