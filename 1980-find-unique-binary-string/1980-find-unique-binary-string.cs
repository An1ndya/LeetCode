public class Solution {
    public string FindDifferentBinaryString(string[] nums) {
        int n  = nums.Length;
        Dictionary < int, bool > hash = new Dictionary < int, bool > ();
        for(int i=0;i<n;i++)
        {
            hash[BinaryStringtoDecimal(nums[i])] = true;
            //Console.Write(BinaryStringtoDecimal(nums[i])); 
        }
        int max= (int)Math.Pow(2,n);
        
        int cur=0;
        while(cur<=max)
        {
            if(!hash.ContainsKey(cur))
            {
                break;
            }
            cur+=1;
        }
        return DecimalToBinaryString(cur).Substring(32-n,n);
    }
    public int BinaryStringtoDecimal(string s) {
        int n  = s.Length;
        int ans=0;
        int powoftwo=1;
        for(int i=n-1;i>=0;i--)
        {
            if(s[i]=='1'){ans+=powoftwo;}
            powoftwo*=2;
        }
        return ans;
    }
    public string DecimalToBinaryString(int n) 
    { 
        string s="";
        // Size of an integer is assumed to be 32 bits 
        for (int i = 31; i >= 0; i--) {    
            if ((n & 1) == 1) 
            {
                s= "1" + s;
            }
            else{
                s= "0" + s;
            }
            n>>=1;
        } 
        return s;
    } 
}