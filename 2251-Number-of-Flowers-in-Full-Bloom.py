class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        lst0=[]
        lst1=[]
        for start,end in flowers:
            lst0.append(start)
            lst1.append(end)
        lst0.sort()
        lst1.sort()
        ret=[0]*len(persons)
        for i in range(len(persons)):
            item=persons[i]
            left=0
            right=len(lst0)
            while left<right:
                middle=left+(right-left)//2
                if lst0[middle]<=item:
                    left=middle+1
                else:
                    right=middle
            while left<len(lst0) and lst0[left]<=item:
                left+=1
            cnt=left
            left=0
            right=len(lst1)-1
            while left<right:
                middle=left+(right-left)//2
                if lst1[middle]<item:
                    left=middle+1
                else:
                    right=middle
            while left>=0 and lst1[left]>=item:
                left-=1
            left+=1
            # print(cnt,left)
            cnt-=left
            ret[i]=cnt
        return ret