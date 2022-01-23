public class Solution {
    public int NumberOfArrays(int[] differences, int lower, int upper) 
    {
        int min=0,max=0,difsum=0;
        
        for(int i=0;i<differences.Length;i++){
            difsum += differences[i];
            if(difsum < min) min = difsum;
            if(difsum > max) max = difsum;
        }
        
        if(Math.Abs(max-min) <= Math.Abs(upper-lower)){
            return Math.Abs(upper-lower)-Math.Abs(max-min)+1;
        }else{
            return 0;
        }
    }
}