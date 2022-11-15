class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        keysSorted = sorted(counter.items(), key = lambda x: x[1], reverse=True)
        return([i[0] for i in keysSorted[:k]])