function validateStackSequences(pushed: number[], popped: number[]): boolean 
{
    let n = pushed.length;
    let stack=[];
    let j=0;
    for(let i=0;i<n;i++)
    {
        stack.push(pushed[i]); 
        while(stack.length && j<n && stack[stack.length-1]==popped[j])
        {
            stack.pop();
            j++;
        }
    }
    return j==n;

};