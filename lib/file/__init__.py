from FunCryptography.lib.logic import *


# This function verifies whether file exist.
def fileExist(name):
    try:
        with open(name, 'rt') as a:
            a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# This function writes into a file and create a new one if doesn't exit.
def writeFile(name, text):
    try:
        a = open(name, 'w+')
    except FileNotFoundError:
        print("ERROR while trying to open file.")
    else:
        try:
            a.write(text)
        except FileNotFoundError:
            print("ERROR while trying to write in file.")
        else:
            a.close()


# This function reads the file text, encode it and copy it into a new string and store it in the variable "b"
def getTextEncoded(name):
    try:
        a = open(name, 'rt')
    except FileNotFoundError:
        print("ERROR while trying to read the file")
    else:
        b = ''
        for line in a:
            encText = encoding(line)
            b = b + encText
        return b


# This function reads the file text, copy it and store into the variable "b". Then turn the text into a list object
# and send it to decoding() function and get the reply resulting of decoding() and return the text into a string.
def getTextDecoded(name):
    try:
        a = open(name, 'rt')
    except FileNotFoundError:
        print("ERROR while trying to read the file")
    else:
        b = ''
        for line in a:
            b = b + line
        lista = list(b)
        showText = decoding(lista)
        return showText
