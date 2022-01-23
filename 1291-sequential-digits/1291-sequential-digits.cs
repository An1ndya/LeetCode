public class Solution {
    public IList<int> SequentialDigits(int low, int high) 
    {
        List<int> ans = new List<int>(); 
        
        int nl = numofdigits(low);
        int nh = numofdigits(high);
        int nd = nl;

        while(nd <= nh)
        {
            int digit = Sequential(nd);
            int one  = ones(nd);
            for(int i=nd;i<=9;i++)
            {
                if(digit>high) return ans;
                else{
                    if(digit>=low) ans.Add(digit); 
                }
                digit += one;
            }
            nd++;
        }
        return ans;
         
    }
    public int numofdigits(int n)
    {
        int d=0;
        while(n!=0)
        {
            n=n/10;
            d++;
        }
        return d;
    }
    public int ones(int n)
    {
        int i=0;
        double number=0;
        while(i<n)
        {
            number+= Math.Pow(10,i);
            i++;
        }
        return Convert.ToInt32(number);
    }
    public int Sequential(int n)
    {
        int i=0;
        double number=0;
        while(i<n)
        {
            number+= (n-i)*Math.Pow(10,i);
            i++;
        }
        return Convert.ToInt32(number);
    }
}