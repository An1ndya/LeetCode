function removeCoveredIntervals(intervals: number[][]): number {
    intervals.sort(comp);
    let n=intervals.length;
    let c=0;
    console.log(intervals)
    let maxend =intervals[0][1];
    for(let i = 1; i < n; i++) {
        if( intervals[i][1] <=maxend)
        {
            c++;
        }else{
            maxend =intervals[i][1]
        }
    }
    return n-c;
};
function comp(a,b) {
    if (a[0] == b[0])
        return b[1] - a[1];
    else
        return a[0] - b[0];
};