function maximumUnits(boxTypes: number[][], truckSize: number): number 
{
    let totalunitbox = 0;
    let n= boxTypes.length;
    boxTypes.sort(function(a,b){ return b[1] - a[1];});
    //console.log(boxTypes);
    for(let i=0;i<n;i++)
    {
        if(boxTypes[i][0]<=truckSize)
        {
            totalunitbox += boxTypes[i][0]* boxTypes[i][1];
            truckSize-=boxTypes[i][0];
        }else{
            totalunitbox += truckSize* boxTypes[i][1];
            break;
        }
    }
    return totalunitbox;
};