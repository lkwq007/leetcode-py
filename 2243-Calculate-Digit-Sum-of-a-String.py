class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            lst=[]
            for i in range(0,len(s),k):
                acc=0
                for j in range(i,min(len(s),i+k)):
                    acc+=int(s[j])
                lst.append(str(acc))
            s="".join(lst)
        return s