import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Returns the maximum number of events you can attend.

        :param events: List[List[int]], where each event is [startDay, endDay].
        :return: int, maximum events attendable.
        """
        # Sort events by start day
        events.sort(key=lambda x: x[0])
        
        min_heap = []   # will store end days of ongoing events
        res = 0         # number of events attended
        day = 0         # current day pointer
        i = 0           # index into sorted events
        n = len(events)
        
        # We only need to iterate days up to the latest end day among all events
        max_end = max(e[1] for e in events) if events else 0
        
        for day in range(1, max_end + 1):
            # Add all events starting today
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            
            # Remove all events that have already ended before today
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # Attend the event that ends earliest (if any)
            if min_heap:
                heapq.heappop(min_heap)
                res += 1
        
        return res
