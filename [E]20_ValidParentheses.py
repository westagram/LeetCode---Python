class Solution:
    def isValid(self, expr: str) -> bool:
        openParentheses = ["[", "{", "("]
        closeParentheses = ["]", "}", ")"]
        pDict = dict(zip(closeParentheses, openParentheses))
        pStack = []
        for i in s:
            if i in openParentheses:
                pStack.append(i)
            else:
                if len(pStack) == 0:
                    return False
                pop = pStack.pop()
                if pop != pDict[i]:
                    return False
        return len(pStack) == 0
