import string

def String(string):
    vowels=str.maketrans({"a":"A","e":"E","i":"I","o":"O","u":"U"})
    return string.translate(vowels)

string=input("Enter a string: ")
print(String(string))