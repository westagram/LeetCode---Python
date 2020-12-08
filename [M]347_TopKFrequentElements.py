class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = dict()
        for n in nums:
            if n in countDict:
                countDict[n] += 1
            else:
                countDict[n] = 1
                
        sortedList = [k for k,v in sorted(countDict.items(), key=lambda x: x[1], reverse = True)]
        return sortedList[:k]