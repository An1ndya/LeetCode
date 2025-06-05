class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        # Initialize each character's parent to itself
        for c in "abcdefghijklmnopqrstuvwxyz":
            parent[c] = c

        # Find with path compression
        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]

        # Union: always attach larger character to smaller one
        def union(c1, c2):
            p1 = find(c1)
            p2 = find(c2)
            if p1 == p2:
                return
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

        # Union all equivalent characters
        for a, b in zip(s1, s2):
            union(a, b)

        # Build final string using the smallest equivalent character
        result = []
        for c in baseStr:
            result.append(find(c))

        return "".join(result)
