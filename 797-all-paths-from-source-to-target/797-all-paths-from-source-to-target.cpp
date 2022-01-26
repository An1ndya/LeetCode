class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) 
    {
        int n = graph.size();
        vector<int> path;
        
        DFS(0,graph,path,n);
        
        return result;
    }
    void DFS(int node,vector<vector<int>>& graph, vector<int> path, int n)
    {
        path.push_back(node);
        
        if(node == n-1)
        {
            result.push_back(path);
            return;
        }
        
        for(int i =0;i<graph[node].size();i++)
        {
            DFS(graph[node][i],graph,path,n);
        }
        
        return;      
    }
};