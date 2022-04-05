function checkArithmeticSubarrays(nums: number[], l: number[], r: number[]): boolean[] 
{
    let  k = l.length;
    let ans =[];
    for(let i=0;i<k;i++)
    {
        let arr = nums.slice(l[i],r[i]+1);
        arr.sort(function(a, b){return a-b;});
        //console.log(arr);
        let dif = arr[1]-arr[0];
        let isArithmetic = true;
        for(let j=2;j<arr.length;j++)
        {
            if(arr[j]-arr[j-1]!= dif)
            {
                isArithmetic = false;
                break;
            }
        }
        ans.push(isArithmetic);
    }
    return ans;
};