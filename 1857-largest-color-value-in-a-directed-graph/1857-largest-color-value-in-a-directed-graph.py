from collections import deque, defaultdict
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # DP table: dp[node][color] -> max count of color along any path ending at node
        dp = [[0] * 26 for _ in range(n)]

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            color_idx = ord(colors[node]) - ord('a')
            dp[node][color_idx] += 1  # include own color

            max_color_value = max(max_color_value, dp[node][color_idx])

            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return max_color_value if visited == n else -1
