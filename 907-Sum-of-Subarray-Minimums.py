class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        term=10**9+7
        ret=0
        acc=0
        # next smaller
        left=[0]*len(arr)
        right=[0]*len(arr)
        stack=[0]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            else:
                left[i]=-1
            stack.append(i)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            else:
                right[i]=len(arr)
            stack.append(i)
        ret=0
        for i in range(len(arr)):
            ret+=(i-left[i])*(right[i]-i)*arr[i]%term
        return ret%term