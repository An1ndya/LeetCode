class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secretKnowntime = [inf]*n
        secretKnowntime[0] = secretKnowntime[firstPerson] = 0
        
        graph = defaultdict(list)
        for meeting in meetings:
            #neighbour with time
            graph[meeting[0]].append((meeting[1],meeting[2]))
            graph[meeting[1]].append((meeting[0],meeting[2]))

        q=[(0,0),(firstPerson,0)]
        #print(graph)
        while q:
            levelcount = len(q)
            while levelcount > 0:
                person, curtime = q.pop(0)
                #print(person, curtime)
                for nextperson, time in graph[person]:
                    #curtime is the time, person know the secret
                    #nextperson cannot know secret from person 
                    #unless meeting take place after
                    #update secretKnowntime if lesser known time found
                    if time >= curtime and secretKnowntime[nextperson] > time:
                        q.append((nextperson,time))
                        secretKnowntime[nextperson] = time
                    
                levelcount-=1
        ans=[]
        for i in range(n):
            if secretKnowntime[i]< inf: ans.append(i)
        return ans