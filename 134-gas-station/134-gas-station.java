class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) 
    {
        int n = gas.length,excess=0,t_excess=0,start=0;
           
        for(int i=0;i<n;i++){
            t_excess += gas[i]-cost[i];
            excess += gas[i]-cost[i];
            
            if (excess < 0)
            {
                //previous station will also break at i 
                //so no need to check previous 
                //continue excess from nxt point 
                excess = 0;
                start = i+1;
            } 
        }
        if (t_excess < 0) return -1;
        else return start;
    }
}