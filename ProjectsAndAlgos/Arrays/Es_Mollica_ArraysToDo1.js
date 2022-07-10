// Push Front
function pushFront (arr, x) {
    for (var i = arr.length ; i > 0; i--){
        arr[i] = arr[i -1];
    }
    arr[0] = x;
    console.log(arr);
    return arr;
}

// Pop Front
function popFront (arr){
    var temp = arr[0];
    for (var i = 0; i < arr.length; i++){
        arr[i] = arr[i + 1];
    }
    arr.length = arr.length -1; 
    console.log(arr);
    // console.log(temp);
    return temp;
}

// Insert At
function insertAt(arr, index, value){
    for (var i = arr.length ; i > index; i--){
        arr[i] = arr[i -1];
    }
    arr[index] = value;
    console.log(arr);
    return arr;
}

pushFront([5,7,2,3], 8); //[8,5,7,2,3]
pushFront([99], 7); //[7,99]

popFront([0,5,10,15]); //0 returned, [5,10,15] printed
popFront([4,5,7,9]); // 4 returned, [5,7,9] printed

insertAt([100,200,5], 2, 311); //[100,200,311,5]
insertAt([9,33,7],1,42); //[9,42,33,7]

