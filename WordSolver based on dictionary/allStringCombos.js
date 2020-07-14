function combine(str){
    const result = [];
    for(let i = 1; i < Math.pow(2, str.length) - 1; i++)
       result.push([...str].filter((_, pos) => {
           return (i >> pos) & 1;
       }).join(""));
   //for(let j=0; j< result.length;j++)
   //{if(result[j].length < 3)}    
   return result;
 }

 console.log(combine("logy"));

 function powerSet( list ){
    var set = [],
        listSize = list.length,
        combinationsCount = (1 << listSize);

    for (var i = 1; i < combinationsCount ; i++ , set.push(combination) )
        for (var j=0, combination = [];j<listSize;j++)
            if ((i & (1 << j)))
                combination.push(list[j]);
    //set = set.toString("");
    return set;
}
console.log(powerSet("logy"));
