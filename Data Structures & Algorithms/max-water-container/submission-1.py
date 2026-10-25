class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left, right = 0, len(heights) - 1

        while left < right :
            value = min(heights[left],heights[right]) * (right - left)
            if value > maximum :
                maximum = value
            
            if heights[left] > heights[right]:
                right -=1
            else :
                left +=1
            
        return maximum