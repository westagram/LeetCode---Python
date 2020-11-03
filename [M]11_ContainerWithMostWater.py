class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1
        
        returnArea = 0
        while left_idx < right_idx:
            curArea = (right_idx - left_idx) * min(height[left_idx], height[right_idx])
            if curArea > returnArea:
                returnArea = curArea
            if height[left_idx] > height[right_idx]:
                right_idx -= 1
            else:
                left_idx += 1
        return returnArea

        
      
