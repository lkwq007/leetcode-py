class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        record=[0]*3
        for item in stones:
            record[item%3]+=1
        total=sum(record)
        # optimally, will not choose to lose
        if total==record[0]:
            return False
        def check(acc,lst):
            local_sum=sum(lst)
            idx=total-local_sum
            alice=False if idx%2 else True
            if local_sum==0:
                return not alice
            if lst[0]>0:
                if lst[0]%2:
                    return not check(acc,[0,lst[1],lst[2]])
                else:
                    return check(acc,[0,lst[1],lst[2]])
            if lst[acc]==0:
                return False
            turns=min(lst[1],lst[2])
            if turns>0:
                return check(acc,[lst[0],lst[1]-turns,lst[2]-turns])
            else:
                lst[acc]-=1
                return not check((acc+acc)%3,lst)
        return (record[1]>0 and (not check(1,[record[0],record[1]-1,record[2]]))) or (record[2]>0 and (not check(2,[record[0],record[1],record[2]-1])))


# class Solution:
#     def stoneGameIX(self, stones: List[int]) -> bool:
#         record=[0]*3
#         for item in stones:
#             record[item%3]+=1
#         total=sum(record)
#         # optimally, will not choose to lose
#         if total==record[0]:
#             return False
#         def check(acc,lst):
#             local_sum=sum(lst)
#             idx=total-local_sum
#             alice=False if idx%2 else True
#             if local_sum==0:
#                 return not alice
#             if lst[0]>0:
#                 if lst[0]%2:
#                     return not check(acc,[0,lst[1],lst[2]])
#                 else:
#                     return check(acc,[0,lst[1],lst[2]])
#             if lst[acc]==0:
#                 return False
#             lst[acc]-=1
#             ret=not check((acc+acc)%3,lst)
#             return ret
#         return (record[1]>0 and (not check(1,[record[0],record[1]-1,record[2]]))) or (record[2]>0 and (not check(2,[record[0],record[1],record[2]-1])))