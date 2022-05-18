class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left=0
        right=len(removable)
        def check(x):
            if x==0:
                return True
            record={}
            for i in range(x):
                record[removable[i]]=1
            idx0=0
            idx1=0
            while idx0<len(s) and idx1<len(p):
                if idx0 in record:
                    idx0+=1
                elif s[idx0]==p[idx1]:
                    idx0+=1
                    idx1+=1
                else:
                    idx0+=1
            return idx1==len(p)
        while left<right:
            middle=left+(right-left)//2
            if check(middle):
                left=middle+1
            else:
                right=middle
        while not check(left):
            left-=1
        return left