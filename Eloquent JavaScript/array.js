function remove(array, index){
         return array.slice(0, index).concat(array.slice(index+1))
           }
console.log(remove([0, 1, 2, 3, 4, 5], 4))
