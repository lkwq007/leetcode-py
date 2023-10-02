class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        ret=maxHeights[0]
        acc=maxHeights[0]
        lst=[0]*len(maxHeights)
        for i in range(1,len(maxHeights)):
            acc=min(maxHeights[i],acc)
            lst[i]=acc
            ret+=acc
        stack=[maxHeights[0]]
        acc=ret
        for i in range(1,len(maxHeights)):
            cur=maxHeights[i]
            if cur>maxHeights[i-1]:
                acc+=cur-maxHeights[i-1]
            else:
                while stack and stack[-1]>cur:
                    top=stack.pop()
                    acc-=top-cur
                if stack:
                    last=stack[-1][-1]
            stack.append(cur)
            if lst[i]!=cur:
                
            ret=max(ret,acc)
        return ret
            
