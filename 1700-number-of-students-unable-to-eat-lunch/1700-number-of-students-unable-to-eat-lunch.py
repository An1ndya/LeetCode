from collections import deque 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        queueStudent = deque(students) 
        queueSandwiches = deque(sandwiches) 
        lastSandwichTakenStep = 0
        #if current n student, none take between last n step, then break
        #means no taking of sandwich is possible
        while lastSandwichTakenStep < n:
            #top student take top sanwich
            if queueStudent[0] == queueSandwiches[0]:
                n -= 1
                lastSandwichTakenStep = 0  #reset count
                queueStudent.popleft()
                queueSandwiches.popleft()
            else:
                lastSandwichTakenStep += 1
                preference = queueStudent.popleft()
                queueStudent.append(preference)
        return n