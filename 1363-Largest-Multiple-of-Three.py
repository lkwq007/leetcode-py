class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # that's not a good solution
        digits.sort(key=lambda x:-x)
        dp=[[] for _ in range(3)]
        for item in digits:
            # print(dp)
            tmp=item%3
            lst=[None]*3
            for i in range(3):
                if len(dp[i])==0:
                    if len(dp[(i-tmp)%3])>0:
                        lst[i]=dp[(i-tmp)%3][:]
                    elif i==tmp:
                        lst[i]=[]
                elif len(dp[(i-tmp)%3])+1>len(dp[i]):
                    lst[i]=dp[(i-tmp)%3][:]
            for i in range(3):
                if lst[i] is None:
                    lst[i]=dp[i]
                else:
                    lst[i].append(item)
            dp=lst
        # print(dp)
        ret="".join(map(str,dp[0]))
        if len(ret)>0 and ret[0]=="0":
            return "0"
        else:
            return ret