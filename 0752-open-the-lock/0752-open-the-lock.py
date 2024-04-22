class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visitedOrDeadend = defaultdict(bool)
        for deadend in deadends:
            visitedOrDeadend[deadend] = True
        #check if starting position is valid or not
        if visitedOrDeadend['0000']: return -1
        #start position
        queue = deque(['0000'])
        move = 0
        #BFS
        while queue:
            n = len(queue)
            for i in range(n):
                lockstring = queue.popleft()
                if lockstring == target: return move
                # 4 charcters
                for j in range(4):
                    # each character can move 2 direction
                    for k in range(2):
                        slot = int(lockstring[j])
                        # increase/decrease count and mod to keep it between 0-9
                        if k == 0: slot = (slot + 1) % 10
                        else:      slot = (slot - 1 ) % 10
                        nextstring = lockstring[0:j] + str(slot) + lockstring[j+1:]
                        if visitedOrDeadend[nextstring] == False:
                            visitedOrDeadend[nextstring] = True
                            queue.append(nextstring)       
            move += 1
        return -1