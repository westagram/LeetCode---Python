class Solution:
    def reverse(self, x: int) -> int:
        strX = "-"+str(x)[1:][::-1] if x<0 else str(x)[::-1]
        if (-2)**31 > int(strX) or int(strX) > (2**31 - 1):
            return 0
        return int(strX)
        
