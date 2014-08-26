function RandomPointOnCircle(radius){
         var angle =Math.random() * 2 * Math.PI
         return {x: radius * Math.cos(angle),
                 y: radius * Math.sin(angle)};
                 }
console.log(RandomPointOnCircle(2))
