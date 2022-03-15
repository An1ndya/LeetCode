function minRemoveToMakeValid(s: string): string 
{
    let n=s.length;
    let stack = [];
    let index = [];
    let i=0;
    let result= "";
    while(i<n)
    {
        if(s[i]=='('){
            stack.push('(');
            index.push(i);
        }else if(s[i]==')'){
            if(stack.length>0 && stack[stack.length-1]=='(')
            {
                stack.pop();
                index.pop();
            }else
            {
                stack.push(')');
                index.push(i);
            }
        } 
        i++;
    }
    let k =0;
    let prev =0;
    while(k<index.length)
    {
        result+=s.slice(prev,index[k]);
        prev=index[k]+1;
        k++;
        
    }
    result+=s.slice(prev,n);
    //console.log(index);
    return result;
};