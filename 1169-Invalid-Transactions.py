class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        record={}
        ret=set([])
        transaction_lst=[]
        for item in transactions:
            lst=item.split(",")
            name,minute,amount,city=lst[0],int(lst[1]),int(lst[2]),lst[3]
            transaction_lst.append((name,minute,amount,city))
        transaction_lst.sort(key=lambda x:x[1])
        for item in transaction_lst:
            name,minute,amount,city=item
            if amount>1000:
                ret.add(f"{name},{minute},{amount},{city}")
            if name not in record:
                record[name]=[]
            bill=record[name]
            flag=False
            pos=-1
            for idx in range(len(bill)):
                loc,time=bill[idx]
                if minute-time<=60 and loc!=city:
                    flag=True
                if loc==city:
                    pos=idx
            if flag:
                ret.add(f"{name},{minute},{amount},{city}")
                if pos>=0:
                    ret.add(f"{name},{bill[pos][1]},{amount},{bill[pos][0]}")
            if pos>=0:
                bill[idx][1]=minute
            else:
                bill.append([city,minute])
        return list(ret)