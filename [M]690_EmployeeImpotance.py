"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importanceMap = collections.defaultdict(int)
        subordinatesMap = collections.defaultdict(list)
        for employee in employees:
            importanceMap[employee.id] = employee.importance
            subordinatesMap[employee.id] = employee.subordinates
        return self.importanceCalc(importanceMap, subordinatesMap, id, 0)

    def importanceCalc(self, importanceMap, subordinatesMap, id, ans):
        if len(subordinatesMap[id]) == 0:
            return ans+importanceMap[id]
        for subordinate in subordinatesMap[id]:
            ans = self.importanceCalc(importanceMap, subordinatesMap, subordinate, ans)
        return ans+importanceMap[id]