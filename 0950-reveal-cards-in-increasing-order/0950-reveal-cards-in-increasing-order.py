class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0] * n
        deck.sort()
        queue = deque()

        # Create a queue of indexes in result array [0,1,2...]
        for i in range(n):
            queue.append(i) 
        
        # Put cards at correct index in result     
        for card in deck:
            # Reveal Card
            result[queue.popleft()] = card

            # Move next card to bottom
            #so, popleft next index and append
            if queue:
                queue.append(queue.popleft())
                
        return result