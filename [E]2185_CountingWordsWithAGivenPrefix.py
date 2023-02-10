class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Create a variable called count to keep track as we loop through the list of words
        # If the prefix matches (using substring), add to count

        count = 0
        pref_length = len(pref)

        for word in words:
            if word[:pref_length] == pref:
                count += 1
        
        return count
