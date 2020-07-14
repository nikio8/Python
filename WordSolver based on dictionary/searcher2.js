function searcher(lookup){
  
    var fs = require("fs") ;
    var text = fs.readFileSync("./dict/dictSmall.txt").toString('utf-8');
    var dictionary = text.split("\r\n") ;
    //console.log(textByLine);

    var indexWord = dictionary.indexOf(lookup);
    if (indexWord>(-1)){
         return lookup + " +++ is legit word.";}
    else {return lookup + " --- not found.";}

}
console.log(searcher("aardvark"));
console.log(searcher("abacus"));
console.log(searcher("niki"));
console.log(searcher("a"));