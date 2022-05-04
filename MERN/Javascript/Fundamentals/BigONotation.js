/*
 * By now we've solved quite a few algorithms, but we may be wondering 
    roughly how long it will take our function to run. One common way to represent 
    this is called Big O Time complexity.
 */

function smallest( arr ) {
        let min = arr[0];
        for( let element of arr ) {
            if( element < min ) {
                min = element;
            }
        }
        return min;
    }
    smallest( [2, 5, 6, 12, 14, 28, 37, 41, 44, 45] );

/*
 * In the above algorithm we will have to look through all 10 items to find the smallest value. 
    As this is the same as the length of the array, it can be said that the algorithm took "N" number of operations, 
    so we would say this algorithm runs in O( N ) time.
 */

function smallest( sortedArr ) {
        return sortedArr[0];
    }
    smallest( [2, 5, 6, 12, 14, 28, 37, 41, 44, 45] );

for(let i=0; i<results.length; i++){
        for(let value of results) {
            for(let j=results.length-1; j>0; j--) {
                console.log(i, value, j);
            }
        }
    }

/*
 * we would say that this runs in O( N^3 ) time. This would be a fairly steep curve and take a lot of time to run. 
    If the length of results is 1000, that console.log would get run 1,000,000,000 times.
 */