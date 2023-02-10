class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreSheet = []
        action = {"+", "C", "D"}
        for operation in operations:
            if operation not in action:
                scoreSheet.append(int(operation))
            else:
                if operation == "+":
                    scoreSheet.append(operator.add(scoreSheet[-1], scoreSheet[-2]))
                elif operation == "C":
                    scoreSheet.pop(-1)
                else:
                    scoreSheet.append(scoreSheet[-1] * 2)
        return sum(scoreSheet)