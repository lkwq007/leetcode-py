class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # reverse
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=0
        queue=record
        while queue:
            target={}
            cnt=0
            for key in queue.keys():
                if key==1:
                    ret+=queue[key]
                elif key==0:
                    continue
                else:
                    cnt+=1
                    target[key//2]=target.get(key//2,0)+queue[key]
                    if key&1:
                        ret+=queue[key]
            if cnt>0:
                ret+=1
            queue=target
        return ret

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret=0
        max_val=1
        for item in nums:
            acc=0
            cnt=0
            while item>0:
                acc+=item&1
                cnt+=1
                item=item>>1
            max_val=max(max_val,cnt)
            ret+=acc
        return ret+max_val-1