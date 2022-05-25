class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        ret=0
        record={}
        for item in milestones:
            record[item]=record.get(item,0)+1
        heap=[-item for item in record.keys()]
        import heapq
        heapq.heapify(heap)
        while heap:
            cur=-heapq.heappop(heap)
            top=-heap[0] if heap else 0
            if record[cur]>1:
                diff=cur-top
                ret+=diff*record[cur]
                record[top]+=record[cur]
                record[cur]=0
            else:
                if top==0:
                    ret+=1
                else:
                    top=-heapq.heappop(heap)
                    next=-heap[0] if heap else 0
                    diff=top-next
                    tmp=diff*record[top]
                    if tmp<=cur-next:
                        ret+=tmp*2
                        if next>0:
                            record[next]+=record[top]
                        record[top]=0
                        record[cur]=0
                        record[cur-tmp]=1
                        heapq.heappush(heap,-(cur-tmp))
                    else:
                        num_top=record[top]
                        num=record[top]-1
                        diff=(cur-top+num-1)//num
                        ret+=diff*num_top*2
                        record[cur]=0
                        record[top]=0
                        tmp=cur-diff*num_top
                        if tmp==top or tmp not in record:
                            heapq.heappush(heap,-tmp)
                            record[tmp]=1
                        else:
                            record[tmp]+=1
                        if top-diff not in record:
                            heapq.heappush(heap,diff-top)
                            record[top-diff]=record[top]
                        else:
                            record[top-diff]+=record[top]
                        record[top]=0
        return ret

# class Solution:
#     def numberOfWeeks(self, milestones: List[int]) -> int:
#         # WA
#         ret=0
#         record={}
#         for item in milestones:
#             record[item]=record.get(item,0)+1
#         lst=list(record.keys())
#         lst.sort(key=lambda x:-x)
#         lst.append(0)
#         record[0]=10**17
#         cur=lst[0]
#         for i in range(1,len(lst)):
#             # print(cur,record[cur],ret,record)
#             if cur==lst[i]:
#                 continue
#             if record[cur]>1:
#                 ret+=record[cur]*(cur-lst[i])
#                 record[lst[i]]+=record[cur]
#                 record[cur]=0
#                 cur=lst[i]
#             else:
#                 if i+1<len(lst):
#                     diff=lst[i]-lst[i+1]
#                     tmp=diff*record[lst[i]]
#                     # print(tmp,cur-lst[i+1])
#                     if tmp<=cur-lst[i+1]:
#                         ret+=tmp*2
#                         record[lst[i+1]]+=record[lst[i]]
#                         record[lst[i]]=0
#                         record[cur]=0
#                         record[cur-tmp]=record.get(cur-tmp,0)+1
#                         cur=cur-tmp
#                     else:
#                         # lst[i]-x >= cur - x*n
#                         # (n-1)*x >= cur -lst[i]
#                         # x >= (cur-lst[i])/(n-1)
#                         num=record[lst[i]]-1
#                         diff=(cur-lst[i]+num-1)//num
#                         ret+=diff*record[lst[i]]*2
#                         record[cur]=0
#                         record[cur-diff*record[lst[i]]]=record.get(cur-diff*record[lst[i]],0)+1
#                         record[lst[i]-diff]=record.get(lst[i]-diff,0)+record[lst[i]]
#                         record[lst[i]]=0
#                         cur=lst[i]-diff
#                 else:
#                     ret+=1
#         return ret