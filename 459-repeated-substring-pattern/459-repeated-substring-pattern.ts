function repeatedSubstringPattern(s: string): boolean 
{
    let n = s.length;
    let len = 1;
    
    for(let len=1;len<=n/2;len++)
    {
        if(n%len==0)
        {
            let j=1;
            for(j=1;j<n/len;j++)
            {
                //console.log(s.substring((j-1)*len, j*len) );
                if(s.substring((j-1)*len, j*len) != s.substring(j*len,(j+1)*len))
                {
                    break;
                }
            }
            if(j==n/len) return true;
        }
    }
    return false;
};