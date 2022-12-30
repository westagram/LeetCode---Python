class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return sorted(counter.items(), key=lambda x: x[1])[-1][0]