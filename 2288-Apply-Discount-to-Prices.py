class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        lst=sentence.split(" ")
        ret=[]
        for word in lst:
            if word[0]=="$" and word[1:].isdigit():
                val=int(word[1:])
                val*=(100-discount)
                if val==0:
                    ret.append("$0.00")
                else:
                    ret.append(f"${val//100}.{(val%100):02}")
            else:
                ret.append(word)
        return " ".join(ret)