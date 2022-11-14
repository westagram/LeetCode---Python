class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumString = "".join(i for i in s if i.isalnum()).lower()
        return alphanumString == alphanumString[::-1]
        
