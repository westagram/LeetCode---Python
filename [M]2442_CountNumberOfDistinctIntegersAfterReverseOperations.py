class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # Create new array that stores the new reversed nums
        # To reverse, convert into a string, and do a reversed

        new_nums = []
        for num in nums:
            new_nums.append(int(str(num)[::-1]))
        return len(set(nums+new_nums))