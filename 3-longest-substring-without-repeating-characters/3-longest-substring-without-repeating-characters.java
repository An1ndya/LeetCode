class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), max = 0,norepeatedcount = 0,i=0, firstsubstringindex=0;
        Map<Character, Integer> isinsubstring = new HashMap<Character, Integer>();
        char temp;
        while(i<n)
        {
            temp = s.charAt(i);
            if(!isinsubstring.containsKey(temp))
            {
                norepeatedcount++;
                if(norepeatedcount > max) max = norepeatedcount;
                isinsubstring.put(temp, i);
                i++;
             
            }
            else
            {
                firstsubstringindex = isinsubstring.get(temp);
                
                isinsubstring.clear();
                //isinsubstring.put(temp, i);
                norepeatedcount = 0;
                i = firstsubstringindex + 1;
                
                
            }
            
            
            
        }
        return max;
    }
}