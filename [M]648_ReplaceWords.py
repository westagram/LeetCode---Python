class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        maxIdx = len(max(dictionary, key=len))
        dictionary = set(dictionary)
        ret = []
        for word in sentence.split():
            exist = ""
            for i in range(maxIdx):
                if word[:i+1] in dictionary:
                    exist = word[:i+1]
                    break
            if exist:
                ret.append(exist)
            else:
                ret.append(word)
        return " ".join(ret)
        