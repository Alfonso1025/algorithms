"""
find duplicate interger in array
"""
array=[1,3,4,3,2,5,1,6]
#return the duplicates of the list
def sort(array):
    if len(array)<1:
        return array
    else:
        doubles=[]
        
        pivot=array.pop()
    greater_pivot=[]
    lower_pivot=[]

    for i in array:
         if(i>pivot):
            greater_pivot.append(i)
         else:
            lower_pivot.append(i)
    
    return sort(lower_pivot) + [pivot] + sort(greater_pivot)

def find_duplicates(arr):
  duplicates=[]
  sorted=  sort(arr)
  print(sorted)
  for i in range(1, len(sorted)):
      #before=sorted[i-1]
      if i==sorted[i-1]:
          print(sorted[i-1])

  return duplicates


print(find_duplicates(array))