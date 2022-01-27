class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target)
    {
        int n = candidates.size();
        vector<int> combo;
        sort(candidates.begin(),candidates.end());
        combinationsum(candidates,combo,n,target,0);
        return result;
    }
    void combinationsum(vector<int>& candidates,vector<int>& combo,int& n, int target,int index)
    {
        if(target < 0)
        {
            return;
        }
        else if(target == 0)
        {
            result.push_back(combo);
            return;
        }
        map <int, bool> m;
        for(int i=index;i<n;i++)
        {   
            if(m[candidates[i]])
            {   
                continue;
            }
            else
            {
                m[candidates[i]]=true;
            }
            combo.push_back(candidates[i]);  
            combinationsum(candidates,combo,n,target-candidates[i],i+1);
            combo.pop_back();
        }        
    }
};