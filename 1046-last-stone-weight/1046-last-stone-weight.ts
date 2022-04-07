
function lastStoneWeight(stones: number[]): number 
{
    stones.sort(function(a, b){return a - b});
    //console.log(stones);
    let n=stones.length;
    while(stones.length>1)
    {
        let max1=stones.pop();
        let max2=stones.pop();
        if(max1!=max2)
        {
            stones.push(Math.abs(max1-max2));
            stones.sort(function(a, b){return a - b});
            //console.log(stones);
        }
    }
    if(stones.length==1) return stones.pop();
    else return 0;
};