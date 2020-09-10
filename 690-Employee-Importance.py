# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.ret=0
        # assume no cycle
        record={}
        for idx,item in enumerate(employees,0):
            record[item.id]=idx
        def dfs(id):
            idx=record[id]
            self.ret+=employees[idx].importance
            for sub in employees[idx].subordinates:
                dfs(sub)
        dfs(id)
        return self.ret