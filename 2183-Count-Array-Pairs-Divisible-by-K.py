class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if k==1:
            return len(nums)*(len(nums)-1)//2
        # gcd?
        def gcd(a,b):
            if a<b:
                a,b=b,a
            while b>0:
                a,b=b,a%b
            return a
        lst=[gcd(item,k) for item in nums]
        record={}
        for item in lst:
            record[item]=record.get(item,0)+1
        ret=0
        for i in range(len(lst)):
            record[lst[i]]-=1
            if lst[i]==k:
                ret+=len(nums)-i-1
            else:
                rest=k//lst[i]
                for key,val in record.items():
                    if key%rest==0 and key>=rest:
                        ret+=val
                # base=rest
                # while rest<=k:
                #     ret+=record.get(rest,0)
                #     rest+=base
        return ret