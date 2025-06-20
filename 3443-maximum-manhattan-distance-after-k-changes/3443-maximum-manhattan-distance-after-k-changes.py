class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # dx, dy for each quadrant 0..3: NE, SE, NW, SW
        signs = [(+1,+1), (+1,-1), (-1,+1), (-1,-1)]
        bad = [0,0,0,0]      # bad[q] = count of moves with contrib = -1 up to current prefix
        ans = 0
        i = 0                # prefix length

        for c in s:
            i += 1
            # step vector
            if c == 'N':
                sx, sy =  0, +1
            elif c == 'S':
                sx, sy =  0, -1
            elif c == 'E':
                sx, sy = +1,  0
            else:  # c == 'W'
                sx, sy = -1,  0

            # update bad-count for each quadrant
            for q, (dx, dy) in enumerate(signs):
                if dx*sx + dy*sy < 0:
                    bad[q] += 1

            # compute best projection for each quadrant
            for q in range(4):
                b = bad[q]
                if b <= k:
                    val = i                # we can flip all bad → good
                else:
                    val = i - 2*(b - k)    # left with (b-k) unflipped bads
                ans = max(ans, val)

        return ans