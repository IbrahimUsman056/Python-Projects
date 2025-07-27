#Write a Python program to translate a message into secret code language. 
# Use the rules below to translate normal English into secret code language.

#ENCODING:
# If the word contains at least three characters, remove the first letter and append it at the end. 
# Now append three random characters at the starting and the end. 
# Else, simply reverse the string.

#DECODING:
#if the word contains less than 3 characters reverse it
#else remove last 3 chars from start and end. now remove last letter and append it to start.

import string
import random

def encode(ibi):
    if(len(ibi)<3):
        newword=ibi[::-1]
    elif(len(ibi)>=3):
        word=ibi[1:]+ibi[0]
        before="".join(random.choices(string.ascii_lowercase,k=3))
        after="".join(random.choices(string.ascii_lowercase,k=3))
        newword=before+word+after
        
    print("Your encoded word is:",newword)

def decode(ibi):
    if(len(ibi)<3):
        newword=ibi[::-1]
    elif(len(ibi)>=3):
        word=ibi[3:-3]
        newword=word[-1]+word[:-1]

    print("Your decoded word is:",newword)


print("Hey! Do you want to encode or decode?")
choice = int(input("1 for encode and 2 for decode: "))
ibi= input("Enter the word:")
match choice:
    case 1:
        encode(ibi)
    case 2:
        decode(ibi)