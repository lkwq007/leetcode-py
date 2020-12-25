import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ret=[0]*len(barcodes)
        record={}
        for item in barcodes:
            record[item]=record.get(item,0)+1
        heap=[(-v,k) for k,v in record.items()]
        heapq.heapify(heap)
        for i in range(len(ret)):
            fisrt=heapq.heappop(heap)
            if i==0 or ret[i-1]!=fisrt[1]:
                ret[i]=fisrt[1]
                if -fisrt[0]>1:
                    heapq.heappush(heap,(fisrt[0]+1,fisrt[1]))
            else:
                second=heapq.heappop(heap)
                if heap and heap[0][0]<second[0]:
                    third=heapq.heappop(heap)
                    heapq.heappush(second)
                    second=third
                ret[i]=second[1]
                if -second[0]>1:
                    heapq.heappush(heap,(second[0]+1,second[1]))
                heapq.heappush(heap,fisrt)
        return ret


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ret=[0]*len(barcodes)
        record={}
        for item in barcodes:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:-record[x])
        idx=0
        for i in range(0,len(ret),2):
            key=keys[idx]
            ret[i]=key
            record[key]-=1
            if record[key]==0:
                idx+=1
        for i in range(1,len(ret),2):
            key=keys[idx]
            ret[i]=key
            record[key]-=1
            if record[key]==0:
                idx+=1
        return ret