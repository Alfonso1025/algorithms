"""
Write a function named capital_indexes. 
The function takes a single parameter,
which is a string. Your function should return 
a list of all the indexes in the string that have capital letters.
"""

def capitals(word):
    #create empty array of capitals
    storeCapitals=[]
    #iterate over string
    for element in word:
    #for each element evaluate if element is capiatl
        if(element==element.upper()):
            wordIndex=word.index(element)
    #append capitals to array_capitals
            storeCapitals.append(wordIndex)
    return storeCapitals

print(capitals('EleonNor'))
