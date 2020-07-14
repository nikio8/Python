function searcher(lookup){
    var dictionary = {"aba":1, "babe":2, "bebs":3, "read":4} ;
    
    var fs = require("fs") ;
    var text = fs.readFileSync("./dict/dictSmall.txt").toString('utf-8');
    var textByLine = text.split("\r\n") ;
    //console.log(textByLine);
    var indexWord = textByLine.indexOf(lookup);
    if (indexWord>(-1)){
         return lookup + " +++ is legit word.";}
    else {return lookup + " --- not found.";}
    //solution = []  ;
    //var solution = dictionary.indexOf(lookup);
    //return dictionary[solution];
    /*if(lookup in textByLine){
        return lookup;
    } */
}

console.log(searcher("aardvark"));
console.log(searcher("abacus"));
console.log(searcher("niki"));
console.log(searcher("a"));