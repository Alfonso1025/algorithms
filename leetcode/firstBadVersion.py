"""
in a sorted array of 0s and 1s, find the first one. 
Solution must have a o(n) complexity
"""
zerosAndOnes=[0,0,0,0,1,1,1,1]
def find_one(arr):
    low=0
    high=len(arr)-1
    firstBad=0
    while low <= high:
        mid=(low+high)//2
        if arr[mid]==1 and arr[mid]-1==0:
            firstBad=arr.index(arr[mid])
            return firstBad
        elif arr[mid]==1:
            mid=low+high//2
        elif arr[mid]==0:
            low=mid+1
    
    return -1




