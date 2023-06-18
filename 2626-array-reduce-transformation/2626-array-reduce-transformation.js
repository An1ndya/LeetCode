/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let n = nums.length;
    if(n==0) return init;
    else{
        let val = init;
        for(let i=0;i<n;i++)
        {
            val = fn(val, nums[i]);
        }
        return val;
    }       
};