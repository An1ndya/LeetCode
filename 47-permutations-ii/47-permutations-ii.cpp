class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        sort(nums.begin(), nums.end());
        permutation(nums,0,nums.size()-1);
        return result;
        
    }
    void permutation(vector<int>& vec, int left, int right)
    {
        if (left == right)
        {
            result.push_back(vec);
            return;
        }
        else
        {
            map <int, bool> m;
            for (int i = left; i <= right; i++)
            {
                if(m[vec[i]])
                {   
                    continue;
                }
                else
                {
                    m[vec[i]]=true;
                }

                swap(vec[left], vec[i]);
                // Recursion called
                permutation(vec, left+1, right);
                //backtrack
                swap(vec[left], vec[i]);         
            }
        }
    }
};