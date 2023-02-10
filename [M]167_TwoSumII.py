class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sIdx, eIdx = 0, len(numbers) - 1
        while numbers[sIdx] + numbers[eIdx] != target:
            total = numbers[sIdx] + numbers[eIdx]
            if total < target:
                sIdx += 1
            elif total > target:
                eIdx -= 1
        return [sIdx+1, eIdx+1]