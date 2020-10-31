class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # len,cnt
        ret_len=0
        ret_cnt=0
        record=[(1,1)]*len(nums)
        for i in range(len(nums)):
            item=nums[i]
            cur=0
            cnt=1
            flag=False
            for j in range(0,i):
                if nums[j]<item:
                    flag=True
                    if record[j][0]>cur:
                        cur=record[j][0]
                        cnt=record[j][1]
                    elif record[j][0]==cur:
                        cnt+=record[j][1]
            if flag:
                record[i]=(cur+1,cnt)
            if record[i][0]>ret_len:
                ret_cnt=record[i][1]
                ret_len=record[i][0]
            elif record[i][0]==ret_len:
                ret_cnt+=record[i][1]
        return ret_cnt

