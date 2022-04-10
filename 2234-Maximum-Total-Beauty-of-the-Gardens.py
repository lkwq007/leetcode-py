class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        complete=0
        record={}
        for item in flowers:
            if item>=target:
                complete+=1
            else:
                record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort()
        left=keys[0]
        right=keys[-1]
        total=newFlowers
        ret=0
        while left<=right and newFlowers>0:
            need=min(target-right,newFlowers)
            cnt=0
            idx=left
            acc=record.get(left,0)
            while need>0:
                if need>=acc:
                    need-=acc
                    cnt+=1
                    acc+=record.get(left+cnt,0)
                else:
                    break
            print(min(target-right,newFlowers),left,acc,cnt)
            num_need=1 if target-right<=newFlowers else 0
            if cnt*partial>full*num_need:
                left=left+cnt
                acc=0
                while idx<left:
                    acc+=record.get(idx,0)
                    idx+=1
                newFlowers-=acc
                record[left]=record.get(left,0)+acc
            else:
                complete+=1
                newFlowers-=target-right
                record[right]=record[right]-1
                while record.get(right,0)==0 and right>left:
                    right-=1
            if cnt==0 and num_need==0:
                break
            print(left,right)
            if newFlowers>=0:
                print(complete,left)
                ret=max(complete*full+left*partial,ret)
            right=max(left,right)
        return ret