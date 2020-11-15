class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x==0:
            return 0
        record={}
        for item in forbidden:
            record[item]=-1
        queue=[(0,0)]
        step=0
        while queue:
            step+=1
            target=[]
            for pos,state in queue:
                next=[]
                if state!=1:
                    next.append((pos-b,1))
                next.append((pos+a,0))
                for next_pos,next_state in next:
                    if next_pos==x:
                        return step
                    if 4000>=next_pos>=0 and next_pos not in record and (next_pos,next_state) not in record:
                        target.append((next_pos,next_state))
                        record[(next_pos,next_state)]=1
            queue=target
        return -1