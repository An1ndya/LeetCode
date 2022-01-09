class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int charfrequency1[]= new int[26];
        Arrays.fill(charfrequency1, 0);
        int n1=s1.length(),n2=s2.length(),index=0;
        if(n1>n2) return false;
        for(int i=0;i<n1;i++) charfrequency1[s1.charAt(i)-'a']++;
        int charfrequency2[]= new int[26];
        Arrays.fill(charfrequency2, 0);
        for(int i=0;i<n2;i++) 
        {
            charfrequency2[s2.charAt(i)-'a']++;
            if(i==n1-1)
            {
               if(Arrays.equals(charfrequency1, charfrequency2)) return true;
            }
            else if(i>=n1)
            {
                charfrequency2[s2.charAt(i-n1)-'a']--;
                if(Arrays.equals(charfrequency1, charfrequency2)) return true;
            }
        }
        return false;
    }
}