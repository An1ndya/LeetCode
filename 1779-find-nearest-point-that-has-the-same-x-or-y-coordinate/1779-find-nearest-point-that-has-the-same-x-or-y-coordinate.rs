impl Solution {
    pub fn nearest_valid_point(x: i32, y: i32, points: Vec<Vec<i32>>) -> i32 
    {
        let mut n = points.len();
        let mut d = 0;
        let mut min = 1000000000;
        let mut mini = -1;
        for i in 0..n
        {
            if(points[i][0]==x || points[i][1]==y)
            {
                d = (points[i][0]-x).abs() + (points[i][1]-y).abs();
                if(d<min)
                {
                    min =d;
                    mini=i as i32
                }
            }
        }
        return mini;
    }
}