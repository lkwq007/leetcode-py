class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if len(A)<2:
            return len(A)
        lst0=[(item,i) for i,item in enumerate(A)]
        lst1=lst0[:]
        lst0.sort()
        lst1.sort(key=lambda x:(-x[0],x[1]))
        # next greater
        greater=[len(A)-1]*len(A)
        smaller=greater[:]
        stack=[]
        for i in range(len(A)-1,-1,-1):
            val,idx=lst0[i]
            while stack and idx>lst0[stack[-1]][1]:
                stack.pop()
            if stack:
                greater[idx]=lst0[stack[-1]][1]
            else:
                greater[idx]=-1
            stack.append(i)
        stack=[]
        for i in range(len(A)-1,-1,-1):
            val,idx=lst1[i]
            while stack and idx>lst1[stack[-1]][1]:
                stack.pop()
            if stack:
                smaller[idx]=lst1[stack[-1]][1]
            else:
                smaller[idx]=-1
            stack.append(i)
        dp=[0]*len(A)
        dp[-1]=1
        even=dp[:]
        odd=dp[:]
        for i in range(len(A)-2,-1,-1):
            if greater[i]!=-1:
                odd[i]=even[greater[i]]
            if smaller[i]!=-1:
                even[i]=odd[smaller[i]]
        return sum(odd)