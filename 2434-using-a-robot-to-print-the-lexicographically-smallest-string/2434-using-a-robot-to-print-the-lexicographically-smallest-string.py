class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_right = [''] * n
        min_right[-1] = s[-1]

        # Precompute the minimum char to the right (including current position)
        for i in range(n - 2, -1, -1):
            min_right[i] = min(s[i], min_right[i + 1])

        t = []
        paper = []
        j = 0

        for i in range(n):
            t.append(s[i])
            # While we can pop from t to paper:
            while t and (j == n - 1 or t[-1] <= min_right[j + 1]):
                paper.append(t.pop())
            j += 1

        # Finally, pop remaining characters in t to paper
        while t:
            paper.append(t.pop())

        return ''.join(paper)