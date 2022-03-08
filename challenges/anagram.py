"""
write a function that takes two strings.
if one string is an anagram of the other, return true. Otherwise,
return false
"""
def anagram(word1,word2):
    #if the lenght of word1 and word2 are different return false
    characters1=[]
    #loop word1 
    for i in word1:
    #count ocurrences of letter in first word
        counter= word1.count(i)
    #store the letter and the count in an object
        word1Obj={
            1:i,
            2:counter
        }
    #store each letter object in a list
        characters1.append(word1Obj)
    #loop word2
    for j in word2:
    #for each word, keep count of ocurrences
        countj=word2.count(j)
    #loop list of letter objects from word1   
        for x in characters1:
    #evaluate if letter in word2 is equal to letter in letter from letter objects
           if j==x[1]:
    #evaluate if the number ofocurences of letter in word2 is 
    # the same as ocurrences in word1
               if countj!=x[2]:
                   print(f"the count of j", {j}, "is", {countj})
               else:
                   print(j,x)




        

    

print(anagram('hello','helo'))
