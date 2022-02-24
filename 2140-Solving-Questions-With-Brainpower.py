class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        ret=questions[-1][0]
        dp=[0]*len(questions)
        dp[-1]=questions[-1][0]
        for i in range(len(questions)-2,-1,-1):
            next=0
            if i+questions[i][1]+1<len(questions):
                next=i+questions[i][1]+1
            dp[i]=max(dp[i+1],dp[next]+questions[i][0])
        return dp[0]