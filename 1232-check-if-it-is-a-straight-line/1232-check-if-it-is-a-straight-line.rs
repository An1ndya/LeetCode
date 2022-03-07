
impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool 
    {
        let mut slope = getslope(coordinates[0].clone(), coordinates[1].clone());
        let mut tslope = vec![0,0];
        
        for i in 2..coordinates.len()
        {
            tslope = getslope(coordinates[i-1].clone(), coordinates[i].clone()); 
            if(slope[0]==0)
            {
                if(tslope[0]!=0){return false;}
            }
            else if(slope[1]==0)
            {
                if(tslope[1]!=0){return false;}
            }else
            {
                if(slope[0]!=tslope[0] || slope[1]!=tslope[1]){return false;}
            }       
        }   
        return true;
        
        pub fn getslope(a:Vec<i32>, b:Vec<i32>)-> Vec<i32>
        {
            let mut dx = a[0]- b[0];
            let mut dy = a[1]- b[1];          
            let gcd = gcd(dx,dy);
            dx=dx/gcd;
            dy=dy/gcd;
            if(dx<0)
            {
                //keeping dx always positive
                dx=-dx;
                dy=-dy;
            }
            return vec![dx,dy];
            
            pub fn gcd(a:i32, b:i32)-> i32
            {
                if(a==0 || b==0){return 1;}
                let mut c = a;
                let mut d = b;
                if(c<0){c=-c;} 
                if(d<0){d=-d;} 
                // do until the two numbers become equal
                while (c != d)
                {
                    // replace the larger number by its difference with the smaller number
                    if (c > d) {
                        c = c - d;
                    }
                    else {
                        d = d - c;
                    }
                }
                return c;        // or `c` (since both are equal)
            }
        }
    }
}