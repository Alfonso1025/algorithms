"""
write a function that takes a string.
the function adds a dot to each letter
"""
def add_dots(word):
    dotsArray=[]
    for l in word:
      dotsArray.append(l)
      dotsArray.append('.')
    return ''.join(dotsArray) 
#print(add_dots('hello'))

def remove_dots(word):
    no_dots=[]
    for l in word:
        if(l!='.'):
            no_dots.append(l)
    return ''.join(no_dots)

print(remove_dots(add_dots('hello')))


