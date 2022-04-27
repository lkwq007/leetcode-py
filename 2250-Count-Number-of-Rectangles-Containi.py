class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        ylst=[[] for i in range(102)]
        for l,h in rectangles:
            ylst[h].append(l)
        for i in range(len(ylst)):
            ylst[i].sort()
        ret=[]
        for x,y in points:
            acc=0
            for i in range(y,len(ylst)):
                if len(ylst[i])==0:
                    continue
                xlst=ylst[i]
                if len(xlst)<10:
                    for item in xlst:
                        if item>=x:
                            acc+=1
                else:
                    left=0
                    right=len(xlst)-1
                    while left<right:
                        middle=left+(right-left)//2
                        if xlst[middle]<x:
                            left=middle+1
                        else:
                            right=middle
                    while left>=0 and xlst[left]>=x:
                        left-=1
                    acc+=len(xlst)-left-1
            ret.append(acc)
        return ret
        