var map ={};
function storePhi(event, phi)
{ map[event] = phi;
}
storePhi("pizza", 0.069);
console.log("pizza" in map); 
console.log(map["pizza"]);
