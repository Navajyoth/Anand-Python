var todolist = []
function rememberto(task){
   todolist.push(task);
}
function whatisnext(){
  return todolist.shift();
}
function urgentlyrememberto(task){
    todolist.unshift(task);
} 
console.log(rememberto("eat"))
console.log(whatisnext())
console.log(todolist[0])




//console.log([1, 2, 3, 2, 1].indexOf(2))
//console.log([1, 2, 3, 2, 1 ].lastIndexOf(2))

