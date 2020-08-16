# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         # [start,end]: start<end
#         lst=[(a,b) for a,b in intervals]
#         intervals=list(set(lst))
#         record={}
#         total=len(intervals)
#         cnt=[0]*total
#         for i in range(total):
#             for j in range(i+1,total):
#                 s1,e1=intervals[i]
#                 s2,e2=intervals[j]
#                 if s1>=e2 or s2>=e1:
#                     continue
#                 if i not in record:
#                     record[i]={}
#                 if j not in record:
#                     record[j]={}
#                 record[i][j]=1
#                 record[j][i]=1
#                 cnt[i]+=1
#                 cnt[j]+=1
#         removed=len(lst)-len(intervals)
#         while len(record)>0:
#             keys=list(record.keys())
#             max_key=keys[0]
#             max_lst=[max_key]
#             for i in range(len(keys)):
#                 key=keys[i]
#                 if cnt[key]>cnt[max_key]:
#                     max_key=key
#                     max_lst=[max_key]
#                 elif cnt[key]==cnt[max_key] and key!=max_key:
#                     max_lst.append(key)
#             if len(max_lst)>1:
#                 selected_key=None
#                 val=None
#                 for key in max_lst:
#                     acc=0
#                     for item in record[key]:
#                         acc+=cnt[item]
#                     if selected_key is None or acc<val:
#                         val=acc
#                         selected_key=key
#                 max_key=selected_key
#             removed+=1
#             for item in record[max_key]:
#                 cnt[item]-=1
#                 del record[item][max_key]
#                 if cnt[item]==0:
#                     del record[item]
#             cnt[max_key]=0
#             del record[max_key]
#         return removed
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<2:
            return 0
        intervals.sort(key=lambda x:(x[1],x[0]))
        end=intervals[0][1]
        cnt=1
        for i in range(1,len(intervals)):
            item=intervals[i]
            if item[0]>=end:
                cnt+=1
                end=item[1]
        return len(intervals)-cnt
