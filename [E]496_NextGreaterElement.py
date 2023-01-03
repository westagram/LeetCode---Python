class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Loop through num2 and create a dict that has the greater element
        # Loop through num1 and append to return list
        ret = []
        masterDict = collections.defaultdict(lambda: -1)
        for idx, num in enumerate(nums2):
            tempIdx = idx + 1
            while tempIdx < len(nums2) and nums2[tempIdx] < num:
                tempIdx += 1
            if tempIdx < len(nums2) and nums2[tempIdx] > num:
                masterDict[num] = nums2[tempIdx]
        for num in nums1:
            ret.append(masterDict[num])
        return ret