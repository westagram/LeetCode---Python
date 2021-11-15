class Solution:
    # def is_overlapped(self, a, b):
    #     return max(a[0], b[0]) <= min(a[1], b[1])
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        sorted_intervals = sorted(intervals, key = lambda i: i[0])
        start_interval = sorted_intervals[0]
        for interval in sorted_intervals[1:]:
            if interval[0] <= start_interval[1]:
                if interval[1] > start_interval[1]:
                    start_interval[1] = interval[1]
                continue
            else:
                output.append(start_interval)
                start_interval = interval
        output.append(start_interval)
        return output
        
        # output = []
        # sorted_interval = sorted(intervals, key = lambda x: x[0])
        # start_interval = sorted_interval[0]
        # for interval in sorted_interval[1:]:
        #     if not self.is_overlapped(start_interval, interval):
        #         output.append(start_interval)
        #         start_interval = interval
        #     else:
        #         start_interval = [min(start_interval[0], interval[0]), max(start_interval[1], interval[1])]
        # output.append(start_interval)
        # return output
