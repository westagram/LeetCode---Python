class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        total = 0
        lastIdx = dict()
        curFruits = []
        for fruitIdx in range(len(fruits)):
            curFruits.append(fruits[fruitIdx])
            lastIdx[fruits[fruitIdx]] = fruitIdx
            if len(lastIdx) > 2:
                removedFruit = list(set(curFruits) - set([fruits[fruitIdx], fruits[fruitIdx-1]]))[0]
                curFruits = fruits[lastIdx[removedFruit]+1:fruitIdx+1]
                del lastIdx[removedFruit]
            total = max(len(curFruits), total)
        return total
            
        
