class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        masterDict = collections.defaultdict(int)
        for n in nums:
            masterDict[n] += 1
        return max(masterDict.values()) > 1