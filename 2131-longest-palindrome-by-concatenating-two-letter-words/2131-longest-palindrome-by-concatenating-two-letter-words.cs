public class Solution {
    public int LongestPalindrome(string[] words) {
        string temp,reverse;
        int n = words.Length,samepair = 0,reversepair = 0, totalsamepair =0;
        Dictionary<string, int> map =  new Dictionary<string, int>();
        for(int i=0;i<n;i++)
        {
            temp = words[i];
 
            if(map.ContainsKey(temp)){
                map[temp]++;  
            }else
            {
                map.Add(temp, 1);
            }
        }
        foreach(var entry in map)
        {
            temp=entry.Key;
            if(temp[0]==temp[1])
            {
                if(entry.Value % 2 == 0) samepair = samepair + entry.Value;
                else samepair = samepair + entry.Value - 1;
                
                totalsamepair = totalsamepair + entry.Value;
            } 
            else if(temp[0]!=temp[1])
            {           
                reverse = temp[1].ToString() + temp[0].ToString();
                if(map.ContainsKey(reverse))
                {
                    reversepair = reversepair + Math.Min(map[reverse], map[temp]); //added two times for each opposite pair
                }
            }
        }
        if(totalsamepair > samepair && samepair % 2 == 0 ) samepair++;
        return 2*reversepair + samepair*2;    
    }
}