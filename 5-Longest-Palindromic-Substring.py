class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force
        ret=[0,0]
        record={}
        even=[None]*len(s)
        odd=[None]*len(s)
        for i in range(len(s)):
            item=s[i]
            odd[i]=set([i])
            even[i]=set([])
            if item in record:
                left=i
                for idx in record[item]:
                    if idx+1==i:
                        even[i].add(idx)
                        left=min(left,idx)
                    elif idx+2==i:
                        odd[i].add(idx)
                        left=min(left,idx)
                    elif idx+1 in even[i-1]:
                        left=min(left,idx)
                        even[i].add(idx)
                    if idx+1 in odd[i-1]:
                        left=min(left,idx)
                        odd[i].add(idx)
                if i-left>ret[1]-ret[0]:
                    ret=[left,i]
                record[item].append(i)
            else:
                record[item]=[i]
        return s[ret[0]:ret[1]+1]


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # WA
#         ret=[0,0]
#         record={}
#         even=[-1]*len(s)
#         odd=[-1]*len(s)
#         for i in range(len(s)):
#             item=s[i]
#             odd[i]=i
#             even[i]=-1
#             if item in record:
#                 for idx in record[item]:
#                     if idx+1==i:
#                         even[i]=min(even[i],idx) if even[i]!=-1 else idx
#                     elif idx+2==i:
#                         odd[i]=min(odd[i],idx)
#                     elif even[i-1]==idx+1:
#                         even[i]=min(even[i],idx) if even[i]!=-1 else idx
#                     elif odd[i-1]==idx+1:
#                         odd[i]=min(odd[i],idx)
#                 if i-even[i]>ret[1]-ret[0] and even[i]!=-1:
#                     ret=[even[i],i]
#                 if i-odd[i]>ret[1]-ret[0]:
#                     ret=[odd[i],i]
#                 record[item].append(i)
#             else:
#                 record[item]=[i]
#         return s[ret[0]:ret[1]+1]
