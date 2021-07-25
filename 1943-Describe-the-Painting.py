class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        start=[(item[0],item[2]) for item in segments]
        end=[(item[1],item[2]) for item in segments]
        start.sort()
        end.sort()
        last=-1
        idx1=0
        idx2=0
        acc=0
        ret=[]
        while idx1<len(start):
            s,c=start[idx1]
            while idx2<len(end) and end[idx2][0]<=s:
                cur,color=end[idx2]
                idx2+=1
                while idx2<len(end) and end[idx2][0]<=cur:
                    color+=end[idx2][1]
                    idx2+=1
                if last!=cur:
                    ret.append([last,cur,acc])
                acc-=color
                if acc==0:
                    last=-1
                else:
                    last=cur
            idx1+=1
            next_color=acc+c
            while idx1<len(start) and start[idx1][0]<=s:
                next_color+=start[idx1][1]
                idx1+=1
            if last!=-1 and last!=s:
                ret.append([last,s,acc])
            acc=next_color
            last=s
        while idx2<len(end):
            cur,color=end[idx2]
            idx2+=1
            while idx2<len(end) and end[idx2][0]<=cur:
                color+=end[idx2][1]
                idx2+=1
            if last!=cur:
                ret.append([last,cur,acc])
            acc-=color
            if acc==0:
                last=-1
            else:
                last=cur
        return ret
