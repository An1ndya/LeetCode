function topKFrequent(nums: number[], k: number): number[] 
{
    let hash= {};
    let ans = [];
    let n=nums.length;
    for(let i=0;i<n;i++)
    {
        if(nums[i] in hash)
        {
            hash[nums[i]]++;
        }else{  
            hash[nums[i]]=1;
        }
    }
    //console.log(hash);
    let sortedkey = getSortedHash(hash);
    //console.log(sortedkey);

    return sortedkey.slice(0,k);
};
function getSortedHash(inputHash){
    var result: number[] = [];
    for(let k in inputHash) result.push(parseInt(k));
    
    result.sort(function(a, b) {
    return inputHash[b] - inputHash[a]
    });
    return result;
}