"""
function that takes a word and  if return true if there 
are two of the letters together eg: hello //ll
"""
def double_letters(word):
    check=0
    for l in word:
        if(l!=check):
            check=l
        else:
            print(check,l)
            return 0

print(double_letters('hello'))
