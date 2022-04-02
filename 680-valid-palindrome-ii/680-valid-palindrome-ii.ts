function validPalindrome(s: string): boolean 
{
    let n = s.length;
    let l=0;
    let r =n-1;
    while(l<r)
    {
        if(s[l]!=s[r])
        {
            return isPalindrome(s.substring(l,r)) || isPalindrome(s.substring(l+1,r+1));
        }
        l++;
        r--;
    }
    return true;
};
function isPalindrome(s: string): boolean 
{
    let n = s.length;
    for(let i=0;i<n/2;i++)
    {
        if(s[i]!=s[n-1-i]) return false;
    }
    return true;
};