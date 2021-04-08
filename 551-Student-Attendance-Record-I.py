class Solution:
    def checkRecord(self, s: str) -> bool:
        absent=0
        acc=0
        flag=True
        for item in s:
            if item=="L":
                acc+=1
                if acc>=3:
                    flag=False
            elif item=="A":
                acc=0
                absent+=1
                if absent>1:
                    flag=False
            else:
                acc=0
        return flag