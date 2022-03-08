const numbers=[2,4,6,7,8,9] //target 5

function bSearch(arr,target){ //mid 2 1
var low=0
var high=arr.length-1// 9

while(low<=high) {

    console.log('this is low ',low)
    console.log('this is high ',high)

    var mid= Math.floor((low+high)/2)//  low=high if mid greater than target return mid-1
    console.log('this is mid: ', mid)
    
    var midElement=arr[mid]//8
    console.log('this is midElement ',midElement)

    
    
    if(midElement===target){
        console.log(mid)
        return mid
    }

    else if(midElement<target){
        console.log('midelement is smaller than target')
         low=mid+1
    }
    else if(midElement>target){
        console.log('midElement is bigger than target')
        high=mid-1
    }
   
}
return low
}
console.log(bSearch(numbers,5))
//const test=Math.floor((5+8)/2)
//console.log(test)s
