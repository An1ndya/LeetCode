class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = {}  # Maps ball label to color
        color_count = {}  # Tracks count of each color
        result = []
        
        for x, y in queries:
            if x in color_map:
                prev_color = color_map[x]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            
            color_map[x] = y
            if y in color_count:
                color_count[y] += 1
            else:
                color_count[y] = 1
            
            result.append(len(color_count))
        
        return result