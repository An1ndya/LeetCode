public class Solution {
    public IList<string> LetterCombinations(string digits) {
        List<string> ans = new List<string>();
        for(int i=0;i<digits.Length;i++)
        {
            List<string> temp = new List<string>(ans);//.Clone();
            ans.Clear();
            
            int size;
            char c = digits[i];
            char first; 
            if(c=='9')
            {
                first = 'w';
                size = 4;
            }
            else if(c=='8')
            {
                first = 't';
                size = 3;
            } 
            else if(c=='7')
            {
                first = 'p';
                size = 4;
            } 
            else
            {
                first = (char)((c-'2')*3+'a');
                size = 3;
            }
            
            int count = temp.Count; 
        
            for(int k=0;k<size;k++)
            {
                char toadd = (char)(first + k);
             
                if(count==0) ans.Add(Char.ToString(toadd));
                else
                {   
                    for(int j=0;j<count;j++)
                    {
                        ans.Add(temp[j]+Char.ToString(toadd));
                    }
                }
            }
        }
        return ans;
    }
}