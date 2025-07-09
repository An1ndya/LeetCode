class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        n = len(startTime)
        gaps = []
        
        # Gap before the first meeting
        first_gap = startTime[0] - 0
        gaps.append(first_gap)
        
        # Gaps between meetings
        for i in range(1, n):
            gap = startTime[i] - endTime[i-1]
            gaps.append(gap)
        
        # Gap after the last meeting
        last_gap = eventTime - endTime[-1]
        gaps.append(last_gap)
        
        max_window = 0
        current_sum = 0
        
        # We need a window of size k+1
        window_size = k + 1
        if window_size > len(gaps):
            return max(gaps)
        
        # Initialize the first window
        for i in range(window_size):
            current_sum += gaps[i]
        max_window = current_sum
        
        # Slide the window
        for i in range(window_size, len(gaps)):
            current_sum += gaps[i] - gaps[i - window_size]
            if current_sum > max_window:
                max_window = current_sum
        
        return max_window