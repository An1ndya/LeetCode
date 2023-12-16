public class Solution {
    public bool IsAnagram(string s, string t) {
        int ns,nt;
        ns = s.Length;
        nt = t.Length;
        if (ns != nt) return false;
        int[] arrs = new int[26];
        int[] arrt = new int[26];
        Array.Fill(arrs,0);
        Array.Fill(arrt,0);
              
        for(int i=0;i<ns;i++)
        {
            arrs[s[i]-'a']++;
        }
        for(int i=0;i<nt;i++)
        {
            arrt[t[i]-'a']++;
        }
        
        for(int i=0;i<26;i++)
        {
            if (arrs[i]!=arrt[i]) return false;
        }
        
        return true;
    }
}