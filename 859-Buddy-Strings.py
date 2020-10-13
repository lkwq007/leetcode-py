class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        lst=[]
        record={"":0}
        for i in range(len(A)):
            if A[i]!=B[i]:
                lst.append(i)
                if len(lst)>2:
                    return False
            record[A[i]]=record.get(A[i],0)+1
        if len(lst)==2:
            return A[lst[0]]==B[lst[1]] and A[lst[1]]==B[lst[0]]
        elif len(lst)==1:
            return False
        else:
            return max(record.values())>1