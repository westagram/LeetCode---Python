class Solution:
    def frequencySort(self, s: str) -> str:
        counter = sorted(collections.Counter(s).items(), key = lambda x: x[1], reverse = True)
        ans = ""
        for pair in counter:
            ans += pair[0]*pair[1]
        return ans