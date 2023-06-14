/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let n = arr.length;
    let filteredArr = [];
    for(let i=0;i<n;i++)
    {
        
        if(Boolean(fn(arr[i],i))) filteredArr.push(arr[i]);
    }
    return filteredArr;
};