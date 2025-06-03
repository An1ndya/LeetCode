from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        queue = deque(initialBoxes)
        haveKey = set()
        haveBoxes = set(initialBoxes)
        res = 0
        opened = set()

        while queue:
            box = queue.popleft()

            if box in opened:
                continue

            # If we can open this box now
            if status[box] == 1 or box in haveKey:
                res += candies[box]
                opened.add(box)

                # Add new keys
                for k in keys[box]:
                    haveKey.add(k)
                    # If you already have the corresponding box — and haven't opened it yet
                    if k in haveBoxes and k not in opened:
                        queue.append(k)

                # Add contained boxes
                for b in containedBoxes[box]:
                    haveBoxes.add(b)
                    queue.append(b)
        return res
