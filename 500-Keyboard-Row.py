from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        rows=list(map(lambda x: x+x.upper(),rows))
        def test(s):
            if s:
                idx=0
                while idx<3:
                    if s[0] in rows[idx]:
                        break
                    idx+=1
                for item in s:
                    if item not in rows[idx]:
                        return False
            return True
            
        return list(filter(test,words))

x=Solution()
print(x.findWords(["qwe","wed"]))