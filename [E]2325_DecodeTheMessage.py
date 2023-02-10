class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        newStr = ""
        repeatTrack = set()
        for char in "".join(key.split()):
            if char not in repeatTrack:
                newStr += char
                repeatTrack.add(char)
        keyMap = dict(zip(newStr, alpha))
        retStr = ""
        for char in message:
            if char in keyMap:
                retStr += keyMap[char]
            else:
                retStr += " "
        return retStr
