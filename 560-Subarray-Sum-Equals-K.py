class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_list=[0]*len(nums)
        idx=0
        total=len(nums)
        acc=0
        sum_table={}
        while idx<total:
            acc+=nums[idx]
            sum_list[idx]=acc
            if acc in sum_table:
                sum_table[acc].append(idx)
            else:
                sum_table[acc]=[idx]
            idx+=1
        for key,val in sum_table.items():
            sum_table[key]=val[::-1]
        idx=0
        cnt=0
        while idx<total:
            val=sum_list[idx]
            if val==k:
                cnt+=1
            next=val+k
            if next in sum_table:
                while sum_table[next] and sum_table[next][-1]<=idx:
                    sum_table[next].pop()
                cnt+=len(sum_table[next])
            idx+=1
        return cnt