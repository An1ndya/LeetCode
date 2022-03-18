function removeDuplicateLetters(s: string): string 
{
    let stack=[];
    let hash = new Map();
    let n=s.length;
    for(let i=0;i<n;i++){hash[s[i]]=i;}
    for(let i=0;i<n;i++)
    {
        if(!stack.includes(s[i]))
        {
            while(stack.length>0 && stack[stack.length-1]>s[i] && hash[stack[stack.length-1]]>i)
            {
                stack.pop();
            }
            stack.push(s[i]);
        }
        
    }
    return stack.join("");
};