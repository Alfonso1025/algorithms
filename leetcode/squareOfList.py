"""
in a list sorted in ascending order, get the square´
of each elemnt while kepping the list sorted in ascending order
exaple: [-5,-4,0,1,2,3] ---[25,,16,0,1,4,9]
        [0,1,4,9,,14,25]
use a double pointer approach
"""
array=[-5,-4,0,1,2,3]

def squares(arr):
    sorted_squares=[]
    start=0
    end=len(arr)-1
    i= len(arr)-1
    

    for i in arr:

        if arr[start]*arr[start]>arr[end]*arr[end]:

            sorted_squares.insert(0,arr[start]*arr[start])
            start=start+1
        else:
            sorted_squares.insert(0,arr[end]*arr[end])
            end=end-1
    return sorted_squares

print(squares(array))