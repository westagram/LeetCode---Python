class Solution:
    from collections import Counter
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return_length = len(p)
        output = []
        p_counter = Counter(p)
        for idx in range(len(s) - return_length+1):
            temp_substring = s[idx:idx+return_length]
            if Counter(temp_substring) == p_counter:
                output.append(idx)
        return output
