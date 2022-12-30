class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        ans = ""
        for idx1 in range(len(s)):
            for idx2 in range(idx1+1, len(s)+1):
                print(s[idx1:idx2], self.isNice(s[idx1:idx2]))
                if self.isNice(s[idx1:idx2]):
                    ans = s[idx1:idx2] if len(s[idx1:idx2]) > len(ans) else ans
        return ans

    def isNice(self, s):
        setSub = set(s)
        for char in setSub:
            if char.islower():
                if char.upper() not in setSub: return False
            else:
                if char.lower() not in setSub: return False
        return True
