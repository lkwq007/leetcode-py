class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst=[]
        for i in range(0,len(s),k):
            lst.append(s[i:i+k])
        for i in range(len(lst)):
            if i%2==0:
                lst[i]=lst[i][::-1]
        return "".join(lst)