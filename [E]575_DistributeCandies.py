class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = len(set(candyType))
        total = int(len(candyType)/2)
        return types if types <= total else total