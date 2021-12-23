class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # 1 <= fruits.length <= 10^5
        # 0 <= startPos, positioni <= 2 * 10^5
        prefix=[0]*(2*k+2)
        left=startPos-k
        right=startPos+k
        for idx,amount in fruits:
            if left<=idx<=right:
                prefix[idx-left]=amount
        for i in range(len(prefix)-1):
            prefix[i]+=prefix[i-1]
        ret=0
        for i in range(1,k+1):
            rest=k-i
            rest=rest//2
            ret=max(prefix[k+i]-prefix[k-rest-1],ret)
            ret=max(prefix[k+rest]-prefix[k-i-1],ret)
        return ret


# class Solution:
#     def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
#         # 1 <= fruits.length <= 10^5
#         # 0 <= startPos, positioni <= 2 * 10^5
#         prefix=[0]*400005
#         left=startPos-k
#         right=startPos+k
#         for idx,amount in fruits:
#             if left<=idx<=right:
#                 prefix[idx-left]=amount
#         for i in range(2*k+1):
#             prefix[i]+=prefix[i-1]
#         ret=0
#         for i in range(2*k+1):
#             if i<k:
#                 l=i
#                 r=k+(i)//2
#                 print(k-l+(r-k)*2)
#             else:
#                 r=i
#                 l=k-(i-k)//2
#                 # print((k-l)*2+r-k)
#             # print(l,r)
#             ret=max(ret,prefix[r]-prefix[l-1])
#         # print(prefix[:2*k])
#         return ret