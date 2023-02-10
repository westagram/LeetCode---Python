class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # Create a tracking var
        # Loop through num, if num - diff and num - diff * 2 in tracking, increase the count
        tracking = set()
        count = 0
        for num in nums:
            if num - diff in tracking and num - (diff * 2) in tracking:
                count += 1
            tracking.add(num)
        return count