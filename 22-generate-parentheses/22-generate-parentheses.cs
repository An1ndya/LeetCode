public class Solution {
    List<string> ans = new List<string>();
    public IList<string> GenerateParenthesis(int n) {
        DFS(n,0,0,"");
        return ans;
    }
    public void DFS(int n,int f,int l,string p)
    {
        if(f+l==2*n)
        {
            ans.Add(p);
            return;
        }
        if(f<n) DFS(n,f+1,l,p+"(");
        if(l<n && l<f)DFS(n,f,l+1,p+")");
    }
    
}