class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        n = len(points)

        # 1) Coordinate compression (separately for x and y)
        xs = sorted(set(x for x, _ in points))
        ys = sorted(set(y for _, y in points))
        x_map = {v: i + 1 for i, v in enumerate(xs)}
        y_map = {v: i + 1 for i, v in enumerate(ys)}

        comp_points = [(x_map[x], y_map[y]) for x, y in points]

        # 2) Sort by x asc, y desc
        comp_points.sort(key=lambda p: (p[0], -p[1]))

        # 3) Build grid and 2D prefix sums (use distinct sizes!)
        size_x = len(xs)
        size_y = len(ys)
        grid = [[0] * (size_y + 2) for _ in range(size_x + 2)]
        for x, y in comp_points:
            grid[x][y] += 1

        prefix = [[0] * (size_y + 2) for _ in range(size_x + 2)]
        for i in range(1, size_x + 1):
            for j in range(1, size_y + 1):
                prefix[i][j] = (grid[i][j]
                                + prefix[i - 1][j]
                                + prefix[i][j - 1]
                                - prefix[i - 1][j - 1])

        def rect_count(x1, y1, x2, y2):
            # inclusive count in rectangle [x1..x2] × [y1..y2]
            if x1 > x2 or y1 > y2:
                return 0
            return (prefix[x2][y2]
                    - prefix[x1 - 1][y2]
                    - prefix[x2][y1 - 1]
                    + prefix[x1 - 1][y1 - 1])

        # 4) Count valid (upper-left, lower-right) pairs
        ans = 0
        for i in range(n):
            xA, yA = comp_points[i]
            for j in range(i + 1, n):
                xB, yB = comp_points[j]
                if xA <= xB and yA >= yB:       # Alice upper-left, Bob lower-right
                    # rectangle is [xA..xB] × [yB..yA]
                    if rect_count(xA, yB, xB, yA) == 2:  # only Alice & Bob
                        ans += 1

        return ans

