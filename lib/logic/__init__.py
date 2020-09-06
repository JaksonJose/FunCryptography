# This function purpose is encoding a text turning a vowel into k + number of 1 to 5 codification.
def encoding(text):
    container = ""
    for letter in text:
        if letter in "a":
            container = container + "k5"
        elif letter in "e":
            container = container + "k4"
        elif letter in "i":
            container = container + "k3"
        elif letter in "o":
            container = container + "k2"
        elif letter in "u":
            container = container + "k1"
        else:
            container = container + letter
    return container


# This function purpose is to decode a text turning the k + number of 1 to 5 codification into a vowel.
# If the first value is a k and the next value is a number among 1 and 5 then it brings a vowel relate with the code.
def decoding(lista):
    container = []
    cont = 0
    while cont < len(lista):
        lista[cont]
        if lista[cont] in 'k' and lista[cont + 1] in '5':
            container.append('a')
            del (lista[1])
        elif lista[cont] in 'k' and lista[cont + 1] in '4':
            container.append('e')
            del (lista[1])
        elif lista[cont] in 'k' and lista[cont + 1] in '3':
            container.append('i')
            del (lista[1])
        elif lista[cont] in 'k' and lista[cont + 1] in '2':
            container.append('o')
            del (lista[1])
        elif lista[cont] in 'k' and lista[cont + 1] in '1':
            container.append('u')
            del (lista[1])
        else:
            container.append(lista[cont])
        cont += 1
    # Turn the list object into string
    texto = ''.join(container)
    return texto


# I wrote this script below for testing the decoding function
'''
frase = "k5mk5nhk5 e 5 de agosto"
# converto o texto string em uma lista (vetor)
lista = (list(frase))
j = decoding(lista)
print(j)
'''
