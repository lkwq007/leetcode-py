class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i=0
        while i<len(s):
            if s[i]=="0":
                break
            i+=1
        while i<len(s):
            if s[i]=="1":
                return False
            i+=1
        return True

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s