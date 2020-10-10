class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if len(A)<2:
            return 0
        stack=[len(A)-1]
        odd_jump=[-1]*len(A)
        for i in range(len(A)-2,-1,-1):
            while stack and A[i]>A[stack[-1]]:
                stack.pop()
            if stack:
                odd_jump[i]=stack[-1]
            stack.append(i)
        stack=[0]
        even_jump=[-1]*len(A)
        for i in range(2,len(A)):
            while stack and A[i]<A[stack[-1]]:
                stack.pop()
            if stack:
                even_jump[i]=stack[-1]
            stack.append(i)
        can_reach=[False]*len(A)
        odd_visited=[False]*len(A)
        even_visited=[False]*len(A)
        jumps=[odd_jump,even_jump]
        visited=[odd_visited,even_visited]
        last=len(A)-1
        print(odd_jump)
        print(even_jump)                                  
        for i in range(len(A)):
            pass
        return 0