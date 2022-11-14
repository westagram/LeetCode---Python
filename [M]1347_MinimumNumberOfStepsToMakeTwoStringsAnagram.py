from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS = Counter(s)
        output = 0
        for char in t:
            if counterS[char] > 0:
                counterS[char] -= 1
            else:
                output += 1
        return output