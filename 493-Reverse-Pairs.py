class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # bit + binary search?
        ret=0
        mapping={}
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        lst=list(record.keys())
        lst.sort()
        for i in range(len(lst)):
            mapping[lst[i]]=i
        cnt=[0]*len(lst)
        def update(idx,val):
            while idx<len(cnt):
                cnt[idx]+=val
                idx=idx|(idx+1)
        def get(idx):
            acc=0
            while idx>=0:
               acc+=cnt[idx]
               idx=(idx&(idx+1))-1
            return acc
        for i in range(len(lst)):
            update(i,record[lst[i]])
        for i in range(len(nums)):
            cur=nums[i]
            query=(cur-1)//2
            left=0
            right=len(lst)
            update(mapping[cur],-1)
            while left<right:
                middle=left+(right-left)//2
                if lst[middle]==query:
                    left=middle
                    break
                elif lst[middle]<query:
                    left=middle+1
                else:
                    right=middle
            if left>=len(lst) or lst[left]>query:
                left-=1
            if left>=0:
                ret+=get(left)
        return ret