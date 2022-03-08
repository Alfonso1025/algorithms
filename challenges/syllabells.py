"""
function takes one string as argument
the string id divided , by syllabels, with a dash.
return the count of syllabels in the string
"""
def syllabells(word):
    count=0
    for l in word:
        if(l=='-'):
          count=count+1
    return count+1
print(syllabells('ket-chup'))

