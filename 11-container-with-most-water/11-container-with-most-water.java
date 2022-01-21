class Solution {
    public int maxArea(int[] height) {
        int max = 0,l,r,n=height.length;
        l = 0;
        r= n-1;
        while ( l<r) {
            int area = (r-l)*Math.min(height[l],height[r]);
            if (area > max ) max = area;
            if (height[l] > height[r]){
                r--;
            }else{
                l++;
            }
        }      
        return max;    
    }
}