class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i=0
        while i<=n:
            #assign new interval  at sorted order
            if  i==n:
                intervals.append(newInterval)
                n+=1
                break
            elif intervals[i][0] > newInterval[0]:
                intervals.insert(i,newInterval)
                n+=1
                break
            else:
                i+=1
        #print(intervals)
        #print(i)
        # merge overlap
        i=1
        while i<n:
            #check for overlapp
            if intervals[i-1][1]>=intervals[i][0]:
                #merged interval to prior element
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
                n-=1
            else:
                i+=1
            #print(i)
        return intervals