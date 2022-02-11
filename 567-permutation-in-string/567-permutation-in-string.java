class Solution {
    public boolean checkInclusion(String s1, String s2) 
    {
                
        int n1=s1.length(), n2=s2.length(), index=0;
        
        if(n1>n2) return false;
        
        int charfrequency1[]= new int[26];
        Arrays.fill(charfrequency1, 0);
        
        int charfrequency2[]= new int[26];
        Arrays.fill(charfrequency2, 0);
        
        for(int i=0;i<n1;i++)  charfrequency1[s1.charAt(i)-'a']++;

        for(int i=0;i<n1;i++)  charfrequency2[s2.charAt(i)-'a']++;
        //check for first n1 length substring
        if(Arrays.equals(charfrequency1, charfrequency2)) return true;
    
        for(int i=n1;i<n2;i++) 
        {
            charfrequency2[s2.charAt(i)-'a']++;
            charfrequency2[s2.charAt(i-n1)-'a']--;
            //check for substring between n1 to n2-1 index substring
            if(Arrays.equals(charfrequency1, charfrequency2)) return true;  
        }
        return false;
    }
}