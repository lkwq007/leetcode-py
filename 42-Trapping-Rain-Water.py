class Solution:
    def trap(self, height: List[int]) -> int:
        greater=[-1]*len(height)
        idx_lst=[0]*len(height)
        stack=[]
        idx=len(height)-1
        while idx>=0:
            item=height[idx]
            while stack:
                if height[stack[-1]]>=item:
                    break
                else:
                    stack.pop()
            if stack:
                idx_lst[idx]=stack[-1]
                greater[idx]=height[stack[-1]]
            else:
                greater[idx]=-1
                idx_lst[idx]=-1
            stack.append(idx)
            idx-=1
        total=len(height)
        idx=0
        acc=0
        while idx<total:
            if greater[idx]!=-1:
                if idx>0 and height[idx-1]>height[idx]:
                    cur_height=min(height[idx-1],height[idx_lst[idx]])
                else:
                    cur_height=height[idx]
                next_boundary=idx_lst[idx]
                while idx<next_boundary:
                    acc+=cur_height-height[idx]
                    idx+=1
            else:
                idx+=1
        return acc