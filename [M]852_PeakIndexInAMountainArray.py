class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        sIdx, eIdx = 0, len(arr) - 1
        mid = (eIdx - sIdx) // 2
        while arr[mid-1] > arr[mid] or arr[mid] < arr[mid+1]:
            if arr[mid-1] > arr[mid]:
                eIdx = mid
            if arr[mid] < arr[mid+1]:
                sIdx = mid
            mid = sIdx + (eIdx - sIdx) // 2
        return mid