# class Solution:
#     def canConstruct(self, s: str, k: int) -> bool:
#         # non-empty
#         if len(s)<k:
#             return False
#         record={}
#         for item in s:
#             record[item]=record.get(item,0)+1
#         odd=0
#         total_odd=0
#         even=0
#         pure_even=0
#         for key,val in record.items():
#             if val&1:
#                 total_odd+=val
#                 odd+=1
#                 if val>1:
#                     even+=val-1
#             else:
#                 even+=val
#                 pure_even+=val
#         even=even//2
#         pure_even=pure_even//2
#         return odd<=k and odd+even>=k or total_odd<=k and total_odd+pure_even>=k
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # non-empty
        if len(s)<k:
            return False
        record={}
        for item in s:
            record[item]=record.get(item,0)+1
        odd=0
        even=0
        for key,val in record.items():
            if val&1:
                k-=1
                if val>1:
                    even+=val-1
            else:
                even+=val
        if k<0:
            return False
        return k<=even
