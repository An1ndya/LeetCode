impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let mut amount = [[0.00f64; 101]; 101];
        amount[0][0]= poured as f64;
        for i in 0..((query_row+1) as usize)
        {
            for j in 0..i+1
            {
                if(amount[i][j]>1.000)
                {
                    let excess= amount[i][j]-1.00;
                    amount[i][j] = 1.00;
                    amount[i+1][j]+=excess/2.0;
                    amount[i+1][j+1]+=excess/2.0;
                }
                //print!("{} ",amount[i][j]);
            }
            //println!("");
        }
        return amount[query_row as usize][query_glass as usize];
    }
}