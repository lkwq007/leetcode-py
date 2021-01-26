class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

class Solution:
    def countSegments(self, s: str) -> int:
        cnt=0
        flag=True
        for item in s:
            if item==" ":
                flag=True
            elif flag:
                cnt+=1
                flag=False
        return cnt