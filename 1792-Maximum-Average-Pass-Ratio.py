import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        acc=0.0
        lst=[]
        for p,total in classes:
            if p==total:
                acc+=1.0
                continue
            lst.append((p/total-(p+1)/(total+1),p,total))
        heapq.heapify(lst)
        while extraStudents>0 and lst:
            top=heapq.heappop(lst)
            extraStudents-=1
            p=top[1]+1
            total=top[2]+1
            heapq.heappush(lst,(p/total-(p+1)/(total+1),p,total))
        for _,p,total in lst:
            acc+=p/total
        return acc/len(classes)