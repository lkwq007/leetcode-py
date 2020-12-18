class Solution:
    def reachNumber(self, target: int) -> int:
        if target==0:
            return 0
        record={0:0}
        step=0
        queue=[0]
        while queue:
            target_queue=[]
            step+=1
            for pos in queue:
                for next in (pos-step,pos+step):
                    if next==target:
                        return step
                    record[next]=step
                    target_queue.append(next)
            queue=target_queue
        return 0