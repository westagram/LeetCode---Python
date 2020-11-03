class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        returnCount = 0
        for char in s:
            if char == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                returnCount += 1
        return returnCount
                
