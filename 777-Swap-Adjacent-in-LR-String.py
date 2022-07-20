class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        idx0=0
        idx1=0
        while idx0<len(start) and idx1<len(end):
            if start[idx0]=="X":
                idx0+=1
                continue
            if end[idx1]=="X":
                idx1+=1
                continue
            if start[idx0]!=end[idx1]:
                return False
            if start[idx0]=="L" and idx0<idx1 or start[idx0]=="R" and idx0>idx1:
                return False
            idx0+=1
            idx1+=1
        idx,lst=(idx0,start) if idx0<len(start) else (idx1,end)
        while idx<len(lst):
            if lst[idx]!="X":
                return False
            idx+=1
        return True
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        target=end
        left=[i for i in range(len(start))]
        right=[i for i in range(len(start))] 
        last=-1
        for i in range(len(start)):
            cur=start[i]
            if cur=="R":
                last=i
            elif cur=="L":
                if last!=-1:
                    left[i]=left[last]+1
                else:
                    left[i]=0
                last=i
        last=len(start)
        for i in range(len(start)-1,-1,-1):
            cur=start[i]
            if cur=="L":
                last=i
            elif cur=="R":
                if last<len(start):
                    right[i]=right[last]-1
                else:
                    right[i]=len(start)-1
                last=i
        idx0=0
        idx1=0
        while idx0<len(start) and idx1<len(target):
            if start[idx0]=="X":
                idx0+=1
                continue
            if target[idx1]=="X":
                idx1+=1
                continue
            if start[idx0]!=target[idx1]:
                return False
            if left[idx0]<=idx1<=right[idx0]:
                idx0+=1
                idx1+=1
            else:
                return False
        while idx0<len(start):
            if start[idx0]!="X":
                return False
            idx0+=1
        while idx1<len(target):
            if target[idx1]!="X":
                return False
            idx1+=1
        return True