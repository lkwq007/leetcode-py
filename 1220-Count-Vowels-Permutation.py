class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n<1:
            return 0
        if n==1:
            return 5
        transition={
            "a":["e"],
            "e":["a","i"],
            "i":["a","e","o","u"],
            "o":["i","u"],
            "u":["a"]
        }
        counter=[1]*5
        term=10**9+7
        idx=2
        acc=5
        while idx<=n:
            next_a=counter[1]+counter[2]+counter[4]
            next_e=counter[0]+counter[2]
            next_i=counter[1]+counter[3]
            next_o=counter[2]
            next_u=counter[2]+counter[3]
            counter=[next_a%term,next_e%term,next_i%term,next_o%term,next_u%term]
            idx+=1
        return sum(counter)%term


x=Solution()
for i in range(100):
    term=10**9+7
    ret=x.countVowelPermutation(i)
    ret2=x.countVowelPermutation(i,True)
    print(ret,ret%term,ret2,ret2%term)
