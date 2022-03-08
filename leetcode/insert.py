"""
In a sorted array, find the given target. If the target
is not present, return the position in which it should be.
For example: target = 4 [1,2,3,5,6,7] 3
             
"""
from tkinter import N


numbers=[1,2,3,4,5,6,8,9]
def find_position(array,target):

    low=0
    high=len(array)-1
    
    while low <= high:
        mid = low + (high - low) //2
        mid_value = array[mid]

        if mid_value == target:
            return mid
        
        elif target < mid_value:
            high=mid-1

        else:
           
            mid=low+1
    return None

#print(find_position(numbers,6))

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

sequence_a = [2,4,5,6,7,8,9,10,13,14]
item_a = 12

print(binary_search(sequence_a, item_a))