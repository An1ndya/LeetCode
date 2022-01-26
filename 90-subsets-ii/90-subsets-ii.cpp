class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> subsetsWithDup(vector<int>& nums) 
    {
        int n = nums.size();
        result.push_back({});
        vector<int> sub;
        //sorting needed to be done to skip duplicate
        sort(nums.begin(), nums.end());
        for(int i=1;i<=n;i++)
        {
            combination(nums,sub,n,i,0,0);
        }

        return result;  
    }
    void combination(vector<int>& nums, vector<int> sub, int n,int k, int count,int index)
    {
        if(count == k)
        {
            result.push_back(sub);
            return;
        }
        if(index >= n)   return;
        if(index + k-count > n) return;
             
        sub.push_back(nums[index]);
        
        combination(nums,sub,n,k,count+1,index+1);
        //remove previusly added call for new combination with next element 
        sub.pop_back();
        //if same, skip duplicate
        while(index+1 < n && nums[index+1]==nums[index]){index++;}
        combination(nums,sub,n,k,count,index+1);          
    }
};