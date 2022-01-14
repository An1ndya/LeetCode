class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> permute(vector<int>& nums) 
    {
        permutation(nums,0,nums.size()-1);
        return result;
    }
    void permutation(vector<int> vec, int left, int right)
    {
        if (left == right)
        {
            result.push_back(vec);
            return;
        }
        else
        {
            for (int i = right; i >= left; i--)
            {
                swap(vec[right], vec[i]);
                // Recursion called
                permutation(vec, left, right-1);
                //backtrack
                //swap(vec[right], vec[i]);
            }
        }
    }
};