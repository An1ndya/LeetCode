func findTheDifference(s string, t string) byte {
    var n,i int    
    n = len(t)
    var ara [26]int
    var ans byte 

    for i=0;i<n;i++{
        ara[t[i]-'a']++
    }
    for i=0;i<n-1;i++{
        ara[s[i]-'a']--
    }
    for i=0;i<26;i++{
        if ara[i] == 1{
            ans = 'a' + byte(i)
        }
    }   
    return ans
}