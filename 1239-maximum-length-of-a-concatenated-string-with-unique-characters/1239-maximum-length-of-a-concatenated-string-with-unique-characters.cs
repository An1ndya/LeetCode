public class Solution {
    public int MaxLength(IList<string> arr) {
        return DFS(ref arr,0,"");
    }
    public int DFS(ref IList<string> arr, int idx, string cursequence) 
    {
        //take remaining unique string one by one 
        int maxlen = 0;
        for(int i = idx; i<arr.Count; i++)
        {
            int count = isuniqueCount(cursequence+arr[i]);
            if (count > 0)
            {
                maxlen = Math.Max(count, maxlen);
                maxlen = Math.Max(maxlen, DFS(ref arr,i+1,cursequence+arr[i]));
            }
        }
        return maxlen;
    }
    public int isuniqueCount(string s)
    {
        //0 if not unique else length
        
        bool[] ischarpresent = new bool[26];
        int len = 0;
        foreach(char c in s)
        {
            int charindex = (int)c - (int)'a';
            if(ischarpresent[charindex] == true)
            {
                return 0;
            } 
            ischarpresent[charindex] = true;
            len++;
        }
        return len;
    }
}