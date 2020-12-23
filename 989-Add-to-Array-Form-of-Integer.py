class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        lst=A[::-1]
        acc=K
        for i in range(len(lst)):
            cur=acc+lst[i]
            acc=cur//10
            lst[i]=cur%10
        while acc>0:
            lst.append(acc%10)
            acc=acc//10
        return lst[::-1]