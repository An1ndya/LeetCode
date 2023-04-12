function simplifyPath(path: string): string 
{
    let stack = [];
    let n= path.length;
    let i = 0;
    while(i<n)
    {
        if(path[i-1]=='/' && path[i]!='/' )
        {
            //new ward
            let start=i;
            while( i <n && path[i]!='/') {   i++; }      
            let dirname = path.substr(start,i-start);
            //console.log(dirname);
            if(dirname == "."){ /*do nothing*/  }
            else if(dirname == "..")
            {
                if(stack.length) stack.pop(); 
            }else{
                stack.push(dirname);
            }
        }
        i++;
    } 
    return "/" + stack.join("/");
};