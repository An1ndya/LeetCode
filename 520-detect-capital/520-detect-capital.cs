public class Solution {
    public bool DetectCapitalUse(string word) 
    {
        int n = word.Length;
        bool isProper = false;
        bool isCap = word[0] >= 'A' && word[0] <= 'Z';

        if(n>=2) isProper = word[1] >= 'A' && word[1] <= 'Z';
        
        for(int i = 1;i<n;i++)
        {
            if(isCap)
            {
                if(isProper)
                {
                    if (word[i] >= 'a' && word[i] <= 'z') return false;
                }
                else
                {
                    if (word[i] >= 'A' && word[i] <= 'Z') return false;
                }    
            }
            else
            {
                if (word[i] >= 'A' && word[i] <= 'Z') return false;
            }
        }
        return true;
    }
}