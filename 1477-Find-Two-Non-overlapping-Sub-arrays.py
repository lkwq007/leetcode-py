class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        acc=0
        prefix=[0]*(len(arr)+1)
        dp=[10**6]*(len(arr)+1)
        record={0:-1}
        ret=10**6
        macc=10**6
        for i in range(len(arr)):
            acc+=arr[i]
            prefix[i]=acc
            last=acc-target
            if last in record:
                macc=min(macc,i-record[last])
                ret=min(ret,i-record[last]+dp[record[last]])
            dp[i]=macc
            
            record[acc]=i
        # print(record,dp)
        if ret>10**5:
            return -1
        return ret