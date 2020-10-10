class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue=["0000"]
        record={}
        for item in deadends:
            record[item]=0
        if "0000" in record:
            return -1
        if target=="0000":
            return 0
        record[0]=1
        step=0
        def alter(x,i):
            # brute force
            lst=list(x)
            cur=int(lst[i])
            lst[i]=str((cur+1)%10)
            up="".join(lst)
            lst[i]=str((cur+10-1)%10)
            down="".join(lst)
            return up,down
        while queue:
            target_q=[]
            step+=1
            for state in queue:
                for i in range(4):
                    for next in alter(state,i):
                        if next==target:
                            return step
                        if next not in record:
                            record[next]=1
                            target_q.append(next)
            queue=target_q
        return -1


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target=int(target)
        if target==0:
            return 0
        queue=[0]
        record={}
        for item in deadends:
            record[int(item)]=0
        if 0 in record:
            return -1
        record[0]=1
        step=0
        offsets=[1,10,100,1000]
        def alter(x,offset):
            left=x//offset
            right=x%offset
            cur=left%10
            left=left//10
            up=(cur+1)%10
            down=(cur+9)%10
            return (left*10+up)*offset+right,(left*10+down)*offset+right
        while queue:
            target_q=[]
            step+=1
            for state in queue:
                for offset in offsets:
                    for next in alter(state,offset):
                        if next==target:
                            return step
                        if next not in record:
                            record[next]=1
                            target_q.append(next)
            queue=target_q
        return -1