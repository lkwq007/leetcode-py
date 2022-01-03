class Solution:
    def checkString(self, s: str) -> bool:
        flag=False
        i=0
        while i<len(s):
            if s[i]=="b":
                flag=True
            if s[i]=="a" and flag:
                return False
            i+=1
        return True