/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: any) {

    return function(n: number): number {
        let low = 1;
        let high = n;
        
        if (isBadVersion(1) === true ) return 1;
        
        while (low < high) 
        {
            let mid = Math.floor((low + high) / 2);
            
            if (low === high-1)
            {
                return high;
            }
            if (isBadVersion(mid) === true )
            {
                high = mid ;
            } 
            else 
            {
                low = mid;
            }
        }
        return low;
    };
};