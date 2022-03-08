"""
A function that takes a string as argument
return the middle letter of the string if no middle letter
return ''
eg: mid(abc) returns 'b'
"""
def find_middle(word):
    lenght= len(word)
    if(lenght%2==0):
        return 'hi'
    divided=lenght/2
    result=divided+.5
    return word[int(result)]

print(find_middle('hello'))