class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T= minutesToTest//minutesToDie
        
        #(T+1)^x >= N
        for i in range(100000):
            if  (T+1)**i>=buckets:
                return i