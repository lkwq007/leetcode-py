class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lst=[0]*(len(s)+1)
        for start,end,d in shifts:
            val=1 if d==1 else -1
            lst[start]+=val
            lst[end+1]-=val
        base=ord("a")
        def alter(c,offset):
            cur=ord(c)-base
            return chr(base+((cur+offset)%26))
        ret=[alter(s[0],lst[0])]
        for i in range(1,len(lst)-1):
            lst[i]+=lst[i-1]
            ret.append(alter(s[i],lst[i]))
        return "".join(ret)