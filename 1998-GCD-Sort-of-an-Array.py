class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        total=max(nums)
        prime=[0]*(total+1)
        plst=[]
        for i in range(2,total+1):
            if prime[i]==0:
                prime[i]=i
                plst.append(i)
            j=0
            while j<len(plst) and plst[j]<=prime[i] and i*plst[j]<=total:
                prime[i*plst[j]]=plst[j]
                j+=1
        disjoint=[-1]*(len(prime)+1)
        group=[[] for _ in disjoint]
        def find(x):
            ret=x
            while disjoint[ret]>=0:
                ret=disjoint[ret]
            while disjoint[x]>=0:
                next=disjoint[x]
                disjoint[x]=ret
                x=next
            return ret
        def union(a,b):
            ai=find(a)
            bi=find(b)
            if ai!=bi:
                if disjoint[ai]>disjoint[bi]:
                    ai,bi=bi,ai
                disjoint[ai]+=disjoint[bi]
                disjoint[bi]=ai
        for i in range(len(nums)):
            head=None
            cur=nums[i]
            for p in plst:
                if p*p>cur:
                    break
                if cur%p==0:
                    if head is None:
                        head=p
                        group[head].append(i)
                    else:
                        union(head,p)
                while cur%p==0:
                    cur=cur//p
            if cur>1:
                if head is None:
                    group[cur].append(i)
                else:
                    union(head,cur)
        record={}
        for p in plst:
            idx=find(p)
            if idx not in record:
                record[idx]=[]
            for item in group[p]:
                record[idx].append(item)
        for k,v in record.items():
            lst=[nums[i] for i in v]
            lst.sort()
            v.sort()
            for a,b in zip(lst,v):
                nums[b]=a
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return False
        return True


# class Solution:
#     def gcdSort(self, nums: List[int]) -> bool:
#         disjoint=[-1]*len(nums)
#         def gcd(a,b):
#             while b>0:
#                 a,b=b,a%b
#             return a
#         def find(x):
#             ret=x
#             while disjoint[ret]>=0:
#                 ret=disjoint[ret]
#             while disjoint[x]>=0:
#                 next=disjoint[x]
#                 disjoint[x]=ret
#                 x=next
#             return ret
#         def union(a,b):
#             ai=find(a)
#             bi=find(b)
#             if ai!=bi:
#                 if disjoint[ai]>disjoint[bi]:
#                     ai,bi=bi,ai
#                 disjoint[ai]+=disjoint[bi]
#                 disjoint[bi]=ai
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if gcd(nums[i],nums[j])>1:
#                     union(i,j)
#         record={}
#         for i in range(len(nums)):
#             idx=find(i)
#             if idx not in record:
#                 record[idx]=[]
#             record[idx].append(i)
#         for k,v in record.items():
#             lst=[nums[i] for i in v]
#             lst.sort()
#             v.sort()
#             for a,b in zip(lst,v):
#                 nums[b]=a
#         for i in range(1,len(nums)):
#             if nums[i]<nums[i-1]:
#                 return False
#         return True