impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 
    {
        let mut sum=0;
        let mut product=1;
        let mut num = n;
        while(num>0)
        {
            let d = num%10;
            product*=d;
            sum+=d;
            num=num/10;
        }
        return product-sum;
    }
}