class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bill=0
        ten_bill=0
        for item in bills:
            if item==5:
                five_bill+=1
            elif item==10:
                if five_bill>0:
                    five_bill-=1
                    ten_bill+=1
                else:
                    return False
            else:
                if ten_bill>0 and five_bill>0:
                    five_bill-=1
                    ten_bill-=1
                elif five_bill>2:
                    five_bill-=3
                else:
                    return False
        return True