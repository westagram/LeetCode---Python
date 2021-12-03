from collections import Counter
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops) != len(bottoms):
            return -1
        total = len(tops)
        same = []
        for idx in range(len(tops)):
            if tops[idx] == bottoms[idx]:
                same.append(tops[idx])
        counterTop, counterBot, counterSame = Counter(tops), Counter(bottoms), Counter(same)
        for i in range(1,7):
            if counterTop[i] + counterBot[i] - counterSame[i] == total:
                return min(counterTop[i] - counterSame[i], counterBot[i] - counterSame[i])
        return -1
            
        
