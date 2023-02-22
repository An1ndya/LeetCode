class Solution {
    public boolean isPerfectSquare(int num) {
        long n = num;
        long low = 1;
        long high = num;
        while (low<high) {
          long mid = (high + low) / 2;
          if (num == 1) {
            return true;
          }
          else if (mid * mid == num) {
            return true;
          }
          else if (mid * mid > num) {
            high = mid - 1;
          }
          else if (mid * mid < num) {
            low = mid + 1;
          }
        }
        if (low * low == num || high * high == num) {
          return true;
        }
        return false;
    }
}