class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counterS = collections.Counter(s)
        ans = ""
        for char in order:
            if char in counterS:
                ans += char*counterS[char]
                del counterS[char]
        for pair in counterS.items():
            ans += pair[0]*pair[1]
        return ans