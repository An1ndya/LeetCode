function strStr(haystack: string, needle: string): number 
{
    let m = haystack.length;
    let n = needle.length;
    
    if(n==0) return 0;
    else if(n>m) return -1;
    
    let i = 0;
    let j = 0
    
    while(i<m)
    {
        if(haystack[i]==needle[j])
        {
            i++;
            j++;
            if(j==n) return i-j;
        }else{
            i=i-j;
            i++;
            j=0;
        }
    }
    return -1;
};