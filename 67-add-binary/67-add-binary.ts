function addBinary(a: string, b: string): string 
{
    let m = a.length;
    let n = b.length;
    let add = 0;
    let i =0;
    let ans = "";
    while(i<m || i<n || add>0)
    {
        if(i<m) add += parseInt(a[m-1-i]);
        if(i<n) add += parseInt(b[n-1-i]);
        //console.log(add);
        ans= (add%2).toString() + ans;
        if(add>1) add=1;
        else add =0;
        
        i++;
    }
    return ans;
};