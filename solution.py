class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        strt = colors[0]
        end = colors[-1]

        max_diff = 0

        for i, color in enumerate(colors):
            if int(strt) != int(color):
                max_diff = max(max_diff, i)
            
        for i, color in enumerate(colors[::-1]):
            if int(end) != int(color):
                max_diff = max(max_diff, i)

        return max_diff