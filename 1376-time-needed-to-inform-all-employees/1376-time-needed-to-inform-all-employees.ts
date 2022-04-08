function numOfMinutes(n: number, headID: number, manager: number[], informTime: number[]): number 
{
    let ans=0;
    //boolean[] isvisited = new boolean[n];
    //Arrays.fill(seats, false)
    for(let i=0;i<n;i++)
    {

        let id= manager[i];
        if(id>=0)
        { 
            let time = 0;
            while(id!=headID)
            {
                time+=informTime[id]; 
                id=manager[id];
                
            }
            
            time+=informTime[id]; 
            ans=Math.max(time, ans);
        }
    }
    return ans;
};