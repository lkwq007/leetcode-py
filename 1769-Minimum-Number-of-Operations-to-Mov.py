class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if len(boxes)<2:
            return [0]
        ret=[0]*len(boxes)
        lacc=0
        racc=0
        lcnt=0
        rcnt=0
        for i in range(len(boxes)):
            if boxes[i]=="1":
                racc+=i
                rcnt+=1
        for i in range(len(boxes)):
            ret[i]=lacc+racc
            if boxes[i]=="1":
                lcnt+=1
                rcnt-=1
            lacc+=lcnt
            racc-=rcnt
        return ret
