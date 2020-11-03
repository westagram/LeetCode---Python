class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIdx = 0
        endIdx = len(nums) - 1
        
        while startIdx <= endIdx:
            midIdx = startIdx + (endIdx - startIdx) // 2
            if nums[midIdx] == target:
                return midIdx
            
            elif nums[midIdx] > target:
                endIdx = midIdx - 1
            
            else:
                startIdx = midIdx + 1
            
        return -1
