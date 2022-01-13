public class Solution {
    public int LongestPalindrome(string s)
    {
        char temp;
        int n = s.Length,count = 0, total = 0;
        Dictionary<char, int> map =  new Dictionary<char, int>();
        for(int i=0;i<n;i++)
        {
            temp = s[i];
 
            if(map.ContainsKey(temp)){
                map[temp]++;  
            }else
            {
                map.Add(temp, 1);
            }
            total++;
        }
        foreach(var entry in map)
        {
            temp = entry.Key;
            if(entry.Value % 2 == 0)
            {
                count = count + entry.Value;    
            }
            else
            {
                count = count + entry.Value-1; 
            }
        }
        if(count < total) count++;
        return count;    
    }
}