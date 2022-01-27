class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) 
    {
        int n = candidates.size();
        vector<int> combo;
        combinationsum(candidates,combo,n,target,0);
        return result;
    }
    void combinationsum(vector<int>& candidates,vector<int> combo,int n, int target,int index)
    {
        //cout<<target<< " "<< index<<endl;
        if(target < 0)
        {
            return;
        }
        else if(target == 0)
        {
            result.push_back(combo);
            return;
        }
        for(int i=index;i<n;i++)
        {         
            combo.push_back(candidates[i]);  
            combinationsum(candidates,combo,n,target-candidates[i],i);
            combo.pop_back();
        }        
    }
};