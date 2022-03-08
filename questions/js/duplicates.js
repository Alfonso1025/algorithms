const dupliArray=[2,3,7,2,8,3,6] 

function duplicates(arr){

   const doubles=[]
   for(let i=0; i<arr.length;i++){
       for(let j=0;j<arr.length;j++){
           if(i!=j){
                if(arr[i]===arr[j]){
                    doubles.push(arr[i])
                }
           }
       }
   }

   return doubles
}
console.log(duplicates(dupliArray))