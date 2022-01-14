class Solution {
public:
    vector<string> result;
    int n;
    vector<string> letterCasePermutation(string s)
    {
        n = s.length();
        permutation(s,0);
        return result;
    }
    void permutation(string s, int i)
    {
        if (i == n)
        { 
            result.push_back(s);
            return;
        } 
        if( 'a' <= s[i] && s[i] <= 'z')
        {    
            permutation(s, i+1);
            
            s[i] = s[i] - 32;
            
            permutation(s, i+1);
    
        }
        else if('A' <= s[i] && s[i] <= 'Z' )
        {           
            permutation(s, i+1);

            s[i] = s[i] + 32;            
            
            permutation(s, i+1);
        }
        else
        {
            permutation(s, i+1);
        }
    }
};