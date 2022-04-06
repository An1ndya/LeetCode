function lemonadeChange(bills: number[]): boolean 
{
    let five=0;
    let ten=0;
    let twenty=0;
    let n = bills.length;
    for(let i=0;i<n;i++)
    {
        if(bills[i]==5) five++;
        else if(bills[i]==10)
        {
            if(five==0) return false;
            five--;
            ten++;
        }
        else if(bills[i]==20)
        {
            if(five==0) return false;
            five--;
            if(ten>0) ten--;
            else if(five>=2) five-=2;
            else return false;
            
            twenty++;
        }
    }
    return true;
};