/**
 *  Sorting an array order by frequency of occurence in javascript
 *  @param {array} array An array to sort
 *  @returns {array} array of item order by frequency
 **/
function customSort(arr) {
    var resultArr = [];
    var num_val = {};
    var tempArr = [];
    var i = 0;
    if(arr.length < 1) throw "arry size too low";

    arr.forEach(function(val) { 
        try { 
            if(val < 1 || val > 1000000) throw "Input value is not valid";
            if(isNaN(val)) throw "not a number";
            if(i > 200000) throw "arry size too high";
        }
        catch(err) {
            console.log('Input ', err);
        }
        if (val in num_val)
            num_val[val] = num_val[val] + 1;
        else
            num_val[val] = 1;
        i += 1;
    });
    

    for(var key in num_val){
        tempArr.push([key, num_val[key]])
    }

    //console.log('temp arr is', tempArr)
    tempArr.sort(function(a, b){
        return a[1] > b[1]
    })

    
    tempArr.forEach(function(obj){
        for(var i=0; i < obj[1]; i++){
            resultArr.push(obj[0]);
        }
    })
    return resultArr;
    
}

console.log(customSort([1]))
console.log(customSort([5,4,3,4,2,2]))
console.log(customSort([10, 2, 1, 4, 2,5, 4,4,4,3,7]))
console.log(customSort([3,0,-1,-2]))
