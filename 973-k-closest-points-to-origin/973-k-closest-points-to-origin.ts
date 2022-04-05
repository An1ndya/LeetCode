function kClosest(points: number[][], k: number): number[][] 
{
    let n= points.length;
    points.sort(function(a, b) 
    {
        let da = Math.sqrt(a[0]*a[0]+a[1]*a[1]);
        let db = Math.sqrt(b[0]*b[0]+b[1]*b[1]);
        if (da < db)    return -1;
        else if (da > db)    return 1; 
        else return 0;
    });
    return points.slice(0,k);
};