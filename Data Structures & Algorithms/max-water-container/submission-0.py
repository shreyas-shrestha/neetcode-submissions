class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        maxArea = 0
        while (L < R):
            smaller = min(heights[L], heights[R])
            tempDist = (R-L) * smaller
            if tempDist > maxArea:
                maxArea = tempDist
            if smaller == heights[L]:
                L = L + 1
            else:
                R = R - 1
        return maxArea


        