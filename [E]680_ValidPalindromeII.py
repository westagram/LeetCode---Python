class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if s == s[::-1]:
        #     return True
        # for idx in range(len(s)):
        #     subStr = s[:idx] + s[idx+1:]
        #     if subStr == subStr[::-1]:
        #         return True
        # return False
        if self.isPalindrome(s):
            return True
        startIdx = 0
        endIdx = len(s) - 1
        while endIdx >= startIdx:
            if s[endIdx] == s[startIdx]:
                endIdx -= 1
                startIdx += 1
                continue
            return self.isPalindrome(s[:startIdx] + s[startIdx+1:]) or self.isPalindrome(s[:endIdx] + s[endIdx+1:])

    def isPalindrome(self, s):
        return s == s[::-1]

