'''
How do you find the missing number 
in a given integer array of 1 to 15?
'''
#array is sorted
from os import startfile


sortedList=[1,2,3,4,5,6,7,8,10,11,12,13,14,15]
#solution 1
def missing_number(sortedArray):
    check=1
    for i in sortedArray:
        if(i==check):
            check=check+1
        else:
            return check

# print(missing_number(sortedList))

#solution 2
def find_missingwith_formula(sorted):
    n=len(sorted)+1
    expectedSum=n*(n+1)/2 
    
    sum=0
    for i in sorted:
        sum=sum+i
    missing= expectedSum-sum
    return missing

#print(find_missingwith_formula(sortedList))

#unsorted array
unsortedList=[15,14,1,2,13,12,3,4,11,10,5,6,8,7]
# for an unsorted array I will use
#  the same function that employs the formula
#print(find_missingwith_formula(unsortedList))
'''
How do you find the missing number 
in a given integer array of 5 to 15?
'''
#with a sorted list
sortedListfromFive=[5,6,7,8,10,11,12,13,14,15]
#solution
def list_fiveTo_fitteen(sorted):
    check=5
    for i in sorted:
        if(i==check):
            check=check+1
        else: 
            return check

#print(list_fiveTo_fitteen(sortedListfromFive))

#unsorted list from five to fifteen
unsortedFiveToFififteen=[15,14,5,6,13,12,7,8,11,10]
#solution
def unsortedList_fiveTo_fifteen(unsorted):
    expectedSum=0
    sum=0
    for i in range(5,16):
        expectedSum=expectedSum+i
    for i in (unsorted):
        sum=sum+i
    missing=expectedSum-sum

    return missing 

#print(unsortedList_fiveTo_fifteen(unsortedFiveToFififteen))

#list is unsorted and both the beggining and end of the list are unknown
anUnsortedList=[8,10,9,5,6]
#solution
def unkown_start_end(unsorted):
    expectedSum=0
    sum=0
    start=unsorted[0]
    end=unsorted[0]
    for i in unsorted:
        sum=sum+i
        if(i<start):
            start=i
        if(i>end):
            end=i
    
    for i in range(start,end+1):
        expectedSum=expectedSum+i

    missing=expectedSum-sum
    return missing

print(unkown_start_end(anUnsortedList))