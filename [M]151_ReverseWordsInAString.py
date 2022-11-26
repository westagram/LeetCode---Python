class Solution:
    def reverseWords(self, s: str) -> str:
        listWords = reversed(s.split())
        retString = ""
        for word in listWords:
            retString += word + " "
        return retString.strip()