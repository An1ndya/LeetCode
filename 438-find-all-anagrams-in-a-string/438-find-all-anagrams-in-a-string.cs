public class Solution {
    public IList<int> FindAnagrams(string s, string p) 
    {
        int ns,np,start,end;
        ns = s.Length;
        np = p.Length;
        List<int> ans = new List<int>();
        
        if(np > ns) return ans;
        
        int[] arrs = new int[26];
        int[] arrp = new int[26];
        Array.Fill(arrs,0);
        Array.Fill(arrp,0);
        
        for(int i=0;i<np;i++)
        {
            arrs[s[i]-'a']++;
            arrp[p[i]-'a']++;
        }
        
        if(IsEqual(arrs,arrp))   ans.Add(0);
        
        start = 0;
        end = np-1;
        while(end <ns-1)
        {
            arrs[s[start]-'a']--;
            start++;
            end++;
            arrs[s[end]-'a']++;
            
            if(IsEqual(arrs,arrp))   ans.Add(start);     
            
        }
        return ans;
    }
    public bool IsEqual(int[] arrs, int[] arrt) {
        
        for(int i=0;i<26;i++)
        {
            if (arrs[i]!=arrt[i]) return false;
        } 
        return true;
    }
}