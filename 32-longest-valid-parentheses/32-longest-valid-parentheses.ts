function longestValidParentheses(s: string): number 
{
    let mx = 0;
    let len = 0;
    let stack = [-1];
    let n = s.length;
    for(let i=0;i<n;i++)
    {
        if(s[i]==')')
        {
            stack.pop();
            if(stack.length==0)
            {
                stack.push(i);
                
            }else{
                len=i-stack[stack.length-1];
                if(len>mx) mx=len;
            }
        }else{
            stack.push(i);
        }      
    }
    return mx;
};