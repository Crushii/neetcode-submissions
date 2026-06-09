class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        max_area = 0
        for i in range(len(heights)):
            j = i+1
            while j < len(heights):
                max_area =max((( j-i ) * min(heights[j] , heights[i])), max_area)
                j+=1


        return max_area


        