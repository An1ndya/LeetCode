public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int n = nums.Count();
        int sum = 0;
        int duplicate = 0;
        int sumwithouterror = n*(n+1)/2;
        Dictionary<int, bool> ispresent = new Dictionary<int, bool>();
        for(int i = 0 ; i < n ; i++)
        {
            if(ispresent.ContainsKey(nums[i]))
            {
                duplicate = nums[i];
            }
            ispresent[nums[i]] = true;
            sum+=nums[i];
        }
        return [duplicate, duplicate + sumwithouterror - sum];
    }
}