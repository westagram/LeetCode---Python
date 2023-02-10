class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Create a map with group size k and list of ppl as value {3:[0,1,2], 1:[5]}}
        # Loop through array, append to list
        groupMap = collections.defaultdict(list)
        for idx, size in enumerate(groupSizes):
            groupMap[size].append(idx)
        retList = []
        for k,v in groupMap.items():
            for idx in range(0, len(v), k):
                retList.append(v[idx:idx+k])
        return retList