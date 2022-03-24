impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 
    {
        let mut stack: Vec<String> = Vec::new();
        let mut ans = 0;
        for str in tokens.iter()
        {
            if(str=="+" || str=="-" || str=="/" || str=="*")
            {
                let a =  stack.pop().unwrap().parse::<i32>().unwrap();
                let b =  stack.pop().unwrap().parse::<i32>().unwrap();
 
                let mut result = 0;
                
                if(str == "+" ){result=b+a;}
                else if(str == "-" ){result=b-a;}
                else if(str == "*" ){result=b*a;}
                else if(str == "/" ){result=b/a;}
                
                stack.push(result.to_string());
            }
            else
            {
                stack.push(str.clone());
            }
        }
        return stack[0].parse::<i32>().unwrap();
    }
}