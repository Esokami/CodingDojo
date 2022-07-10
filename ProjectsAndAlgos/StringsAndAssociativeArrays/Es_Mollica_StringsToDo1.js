// Remove Blanks
function removeBlanks(str){
    var newStr = " ";
    for (var i = 0; i < str.length; i++){
        if(str[i] != " "){
            newStr += str[i];
        }
    }
    console.log(newStr);
}

// Get Digits
function getDigits(str){
    var digits = " ";
    for (i = 0; i < str.length; i++){
        if (!isNaN(str[i])){
            digits += str[i];
        }
    }
    console.log(digits);
}

//Acronyms
function acronyms(str){
    var splitStr = str.split(" ");
    var acro = " ";
    for (i = 0; i < splitStr.length; i++){
        if (splitStr[i].length > 0){
            acro += splitStr[i][0].toUpperCase();
        }
    }
    console.log(acro);
}

//Count Non-Spaces
function countNonSpaces(str){
    var count = 0;
    for (var i =0; i < str.length; i++){
        if(str[i] != " "){
            count++;
        }
    }
    console.log(count);
}

//Remove Shorter Strings
function removeShorterStrings(arr, num){
    var newArr = [];
    for (i = 0; i < arr.length; i++){
        if (arr[i].length >= num){
            newArr.push(arr[i])
        }
    }
    console.log(newArr);
}

removeBlanks(" Pl ayTha tF u nkyM usi c "); //"PlayThatFunkyMusic"
removeBlanks("I can not BELIEVE it's not BUTTER"); //"IcannotBELIEVEit'snotBUTTER"

getDigits("abc8c0d1ngd0j0!8"); //801008
getDigits("0s1a3y5w7h9a2t4?6!8?0"); //1357924680

acronyms(" there's no free lunch - gotta pay yer way. "); //"TNFL-GPYW"
acronyms("Live from New York, it's Saturday Night!"); //"LFNYISN"

countNonSpaces("Honey pie, you are driving me crazy"); //29
countNonSpaces("Hello world !"); //11

removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4);
// //['Good morning', 'sunshine', 'Earth', 'says', 'hello']
removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3);
// //['There', 'bug', 'the', 'system']