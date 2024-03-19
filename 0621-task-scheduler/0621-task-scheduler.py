class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = [0]*26
        for task in tasks:
            taskCount[ord(task) - ord('A')] += 1
        taskCount.sort(reverse=True)
        #maxtaskCount = taskCount[0]
        #so idle cool down set between them is
        cooldownset  = taskCount[0] -1
        #here is the idle cycle between like the dot between A..A..A
        idleCycle = cooldownset * n 
        #we will check if we can fit other task(except A) during this cooldown
        #start with next highest count
        for i in range(1,26):
            #if current task count is more than cooldownset 
            #means some will go at last end of A: case like A=3, B=3
            #outside A is not included in idleCycle 
            idleCycle -= min(cooldownset, taskCount[i])
        if idleCycle > 0:
            return len(tasks) + idleCycle
        else:
            #all task compacted, no idleCycle between
            return  len(tasks)
        