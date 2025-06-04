class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word  # special case: whole word is one part

        n = len(word)
        if numFriends > n:
            return ""

        max_len = n - numFriends + 1
        best_start = 0

        for i in range(1, n):
            j = 0
            while j < max_len and i + j < n and word[best_start + j] == word[i + j]:
                j += 1
            if j < max_len and i + j < n and word[i + j] > word[best_start + j]:
                best_start = i

        return word[best_start: best_start + max_len]