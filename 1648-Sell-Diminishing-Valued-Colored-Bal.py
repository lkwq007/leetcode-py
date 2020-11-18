class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        term=10**9+7
        if orders==1:
            return max(inventory)
        record={}
        for item in inventory:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:-x)
        ret=0
        record[0]=0
        for i in range(len(keys)):
            key=keys[i]
            next=keys[i+1] if i<len(keys)-1 else 0
            val=record[key]
            total=(key-next)*val
            if total<orders:
                orders-=total
                # record[key]=0
                record[next]+=val
                acc=(key-next)*(key+next+1)//2
                ret=(ret+acc*val)%term
            else:
                num=orders//val
                rest=orders%val
                acc=val*num*(key+key-num+1)//2+rest*(key-num)
                ret=(ret+acc)%term
                break
        return ret