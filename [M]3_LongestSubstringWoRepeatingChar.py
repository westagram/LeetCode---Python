class Solution(object):
    def lengthOfLongestSubstring(self, s):
        nonRepeat = []
        largest = 0
        for char in s:
            if char in nonRepeat:
                idx = nonRepeat.index(char)
                nonRepeat = nonRepeat[idx+1:]
            nonRepeat.append(char)
            if len(nonRepeat) > largest:
                largest = len(nonRepeat)
                
        return largest
        
