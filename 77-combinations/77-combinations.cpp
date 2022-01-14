class Solution {
public:
    vector<vector<int>> result;
    int end,maxcount;
    vector<vector<int>> combine(int n, int k) 
    {
        end=n-1,maxcount=k;
        vector<int> data;
        int arr[n];
        for(int i=0;i<n;i++)  arr[i] = i+1;
        
        combination(arr,data,0,0);
        return result;
    }
    void combination(int arr[], vector<int> data,int start,int count)
    {
        //for(int i = 0;i<data.size();i++) cout<<" "<<data[i];
        //cout<< " start "<<start << " count "<<count<<endl;
        
        // Current combination is ready
        if (count == maxcount)
        {
            result.push_back(data);
            return;
        }
        // replace index with all possible
        //The condition "end-i+1 >= maxcount - count"//geekforgeeks
        // makes sure that including one element
        // at index will make a combination with
        // remaining elements at remaining positions
        for (int i = start; i <= end ; i++)
        {
            //return correct without condition but makes time efficient
            //beacuse if  i + maxcount-count > n then recursion wont find any suitable combination
            //as from i + remaining numbers wont fill maxcount
            if(end + 1 >= i + maxcount - count)
            {
                data.push_back(arr[i]);
                combination(arr, data, i+1, count+1);
                data.pop_back();
            }
        }
    }
};