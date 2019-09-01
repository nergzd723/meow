# Fast inmethod encrypting tool
# Not safe
# Uses Caesar Encryption
# The key is based on lenght of message
# By Mark Hargreaves
# GNU LGPL v3

import sys
import random

def getkey(mesg):
    f = 0
    mrth = mesg[-6:]
    while(f != 27):
        f += 1
        ra = decaesar(f, mrth)
        if ra == 'martha':
            break
    if f == 27:
        print("Decryption failed! Message is corrupted or MAGIC is not there")
        exit(0)
    return f

def genkey(mesg):
    k1 = len(mesg)
    k2 = random.randint(-15, 20)
    key = k1+k2
    key = abs(key)
    while key > 26:
        key = key-26
        print(key)
    return key

def caesar(key, message):
    message = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in message:
      if letter in alpha:
          letter_index = (alpha.find(letter) + key) % len(alpha)
          result = result + alpha[letter_index]
      else:
          result = result + letter
    return result
def decaesar(key, message):
    message = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in message:
      if letter in alpha:
        letter_index = (alpha.find(letter) - key) % len(alpha)
        result = result + alpha[letter_index]
      else:
        result = result + letter
    return result
a = sys.argv[1:]
if not a:
    cin = input("Enter message or DEC to decrypt ")
    if cin = 'DEC':
        cin = input('Enter text to decrypt ')
        k = getkey(cin)
        rath = decaesar(k, cin)
        print(rath[:-6])
        exit()        
else:
    if '-d' in a:
        cin = a[1]
        k = getkey(cin)
        rath = decaesar(k, cin)
        print(rath[:-6])
        exit()
    cin = a[0]
key = genkey(cin)
cint = cin+'martha'
r = caesar(key, cint)
print('Encrypted message', r)
