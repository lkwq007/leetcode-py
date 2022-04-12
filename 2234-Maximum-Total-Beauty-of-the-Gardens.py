class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        complete=0
        lst=[]
        for item in flowers:
            if item>=target:
                complete+=1
            else:
                lst.append(item)
        lst.sort()
        suffix=[0]*len(lst)
        acc=0
        cnt=0
        for i in range(len(lst)-1,-1,-1):
            acc+=target-lst[i]
            suffix[i]=acc
            if suffix[i]<=newFlowers:
                cnt=len(lst)-i
        suffix.append(0)
        ret=(cnt+complete)*full
        if len(lst)<1:
            return ret
        acc=0
        idx=0
        cnt=0
        right=0
        for l in range(lst[0],target):
            acc+=cnt
            while idx<len(lst) and lst[idx]<=l:
                idx+=1
                cnt+=1
            if acc>newFlowers:
                break
            rest=newFlowers-acc
            while right<len(lst) and suffix[right]>rest:
                right+=1
            if right>=idx:
                total=len(lst)-right
            else:
                total=len(lst)-idx
                total+=min(cnt-1,(rest-suffix[idx])//(target-l))
            # to make sure this works, at least one should have val l
            possible=total
            ret=max(ret,(possible+complete)*full+l*partial)
        return ret

# class Solution:
#     def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
#         complete=0
#         record={}
#         for item in flowers:
#             if item>=target:
#                 complete+=1
#             else:
#                 record[item]=record.get(item,0)+1
#         keys=list(record.keys())
#         keys.sort()
#         left=keys[0]
#         right=keys[-1]
#         total=newFlowers
#         ret=0
#         iter=0
#         while left<=right and newFlowers>0 and right<target and complete<len(flowers):
#             iter+=1
#             need=min(target-right,newFlowers)
#             cnt=0
#             idx=left
#             acc=record.get(left,0)
#             while need>0:
#                 if need>=acc:
#                     need-=acc
#                     cnt+=1
#                     acc+=record.get(left+cnt,0)
#                 else:
#                     break
#             print(min(target-right,newFlowers),left,acc,cnt)
#             num_need=1 if target-right<=newFlowers else 0
#             if left+cnt==target:
#                 cnt-=1
#             if cnt*partial>full*num_need:
#                 left=left+cnt
#                 acc=0
#                 while idx<left:
#                     acc+=record.get(idx,0)
#                     idx+=1
#                 newFlowers-=acc
#                 record[left]=record.get(left,0)+acc
#             else:
#                 complete+=1
#                 newFlowers-=target-right
#                 record[right]=record[right]-1
#                 while record.get(right,0)==0 and right>left:
#                     right-=1
#             if cnt==0 and num_need==0:
#                 break
#             print(left,right)
#             if newFlowers>=0:
#                 print(complete,left)
#                 if left==target:
#                     ret=max(ret,len(flowers)*full)
#                 else:
#                     ret=max(complete*full+left*partial,ret)
#             right=max(left,right)
#         return ret