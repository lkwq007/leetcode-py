class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ERROR
        if len(prices)<2:
            return 0
        # continuous, not matter
        last=0
        total=0
        idx=1
        while idx<len(prices):
            if prices[idx]>prices[idx-1]:
                last=prices[idx]-prices[idx-1]
                total+=last
                idx+=1
            else:
                if idx+1>=len(prices) or prices[idx+1]<=prices[idx]:
                    last=0
                    idx+=1
                elif prices[idx+1]>prices[idx]:
                    total-=last
                    cur=max(prices[idx+1]-prices[idx-1],last,prices[idx+1]-prices[idx])
                    total+=cur
                    idx+=2
        return total


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        # preprocessing
        lst=[[0,-2,-2]]
        state=0
        idx=0
        template=[0,-1,-1]
        acc=template[:]
        while idx+1<len(prices):
            if prices[idx]<prices[idx+1]:
                diff=prices[idx+1]-prices[idx]
                acc[0]+=diff
                if acc[1]<0:
                    acc[1]=idx
                acc[2]=idx+1
            else:
                if acc[0]>0:
                    lst.append(acc)
                    acc=template[:]
            idx+=1
        if acc[0]>0:
            lst.append(acc)
        idx=1
        ret=0
        print(lst)
        while idx<len(lst):
            diff,first,last=lst[idx]
            prev_diff,prev_first,prev_last=lst[idx-1]
            if prev_last+1!=first:
                ret+=prev_diff
                print(idx)
            else:
                seg1=prices[prev_last]-prices[prev_last-1]
                seg2=prices[first+1]-prices[first]
                tmp=[prices[last]-prices[prev_first],prev_diff-seg1+diff,prev_diff+diff-seg2]
                max_idx=0
                for i in range(1,3):
                    if tmp[max_idx]<tmp[i]:
                        max_idx=i
                print(idx,max_idx)
                max_diff=tmp[max_idx]
                lst[idx][0]=max_diff
                if max_idx==0:
                    lst[idx][1]=prev_first
                elif max_idx==2:
                    lst[idx][1]=first+1
            idx+=1
        return lst[-1][0]+ret