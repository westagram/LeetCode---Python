class Solution:
    def isOverlapped(self, a, b):
        return max(a[0], b[0]) <= min(a[1], b[1])
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for idx in range(len(intervals)):
            if not self.isOverlapped(intervals[idx], newInterval):
                output.append(intervals[idx])
            else:
                newInterval = [min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])]
            
        output.append(newInterval)
        return sorted(output, key = lambda x: x[0])
