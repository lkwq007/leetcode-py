class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        if len(orders)<1:
            return []
        food_item={}
        table={}
        for _,table_no,food in orders:
            food_item[food]=1
            table_no=int(table_no)
            if table_no not in table:
                table[table_no]={}
            table[table_no][food]=table[table_no].get(food,0)+1
        keys=list(food_item.keys())
        keys.sort()
        ret=[["Table"]]
        ret[0].extend(keys)
        table_keys=list(table.keys())
        table_keys.sort()
        for n in table_keys:
            ret.append([str(n)])
            for item in keys:
                ret[-1].append(str(table[n].get(item,0)))
        return ret