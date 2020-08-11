class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        record={}
        ret=[]
        for item in transactions:
            lst=item.split(",")
            name,minute,amount,city=lst[0],int(lst[1]),int(lst[2]),lst[3]
            if amount>1000:
                continue