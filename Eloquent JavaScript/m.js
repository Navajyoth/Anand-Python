function sortfreq(freqs)
{
group=[];
for(var keys in freqs)
group.push([freqs[keys],keys]);
return(group.sort());
}
groups=sortfreq({'a':3,'b':2,'c':1});
console.log(groups);

