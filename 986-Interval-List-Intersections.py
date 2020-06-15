class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A)<1 or len(B)<1:
            return []
        ret=[]
        i=0
        j=0
        totalA=len(A)
        totalB=len(B)
        while i<totalA and j<totalB:
            lo=max(A[i][0],B[j][0])
            hi=min(A[i][1],B[j][1])
            if lo<=hi:
                ret.append([lo,hi])
            if hi==A[i][1]:
                i+=1
            else:
                j+=1
        return ret

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A)<1 or len(B)<1:
            return []
        lst=[]
        for start,end in A:
            lst.append((start,0))
            lst.append((end,1))
        for start,end in B:
            lst.append((start,2))
            lst.append((end,3))
        lst.sort(key=lambda x:x[0])
        stack=[]
        ret=[]
        lastA=-1
        lastB=-1
        for pos,state in lst:
            if state==0 or state==2:
                stack.append((pos,state))
                if state==0 and lastB==pos or state==2 and lastA==pos:
                    ret.append([pos,pos])
            elif state==1:
                if stack[-1][1]==0:
                    top=stack.pop()
                    if stack:
                        ret.append([top[0],pos])
                else:
                    top=stack.pop()
                    tmp=stack.pop()
                    stack.append(top)
                    ret.append([top[0],pos])
                lastA=pos
            else:
                if stack[-1][1]==2:
                    top=stack.pop()
                    if stack:
                        ret.append([top[0],pos])
                else:
                    top=stack.pop()
                    tmp=stack.pop()
                    stack.append(top)
                    ret.append([top[0],pos])
                lastB=pos
        return ret