from typing import List
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # TLE
        masks={}
        mask=1
        for i in range(26):
            item=chr(ord("a")+i)
            masks[item]=mask
            mask=mask<<1
        def convert(s):
            ret=0
            for item in s:
                ret|=masks[item]
            return ret
        puzzle_bits=[(convert(item),masks[item[0]]) for item in puzzles]
        word_bits=[convert(item) for item in words]
        ret=[0]*len(puzzles)
        for idx in range(len(puzzles)):
            puzzle,first=puzzle_bits[idx]
            cnt=0
            for item in word_bits:
                if item&first and (puzzle|item)^puzzle==0:
                    cnt+=1
            ret[idx]=cnt
        return ret

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        masks={}
        mask=1
        for i in range(26):
            item=chr(ord("a")+i)
            masks[item]=mask
            mask=mask<<1
        record={}
        def convert(s):
            ret=0
            for item in s:
                ret|=masks[item]
            return ret
        def construct(item,base,idx):
            if item:
                mask=masks[item[0]]
                construct(item[1:],base|mask,idx)
                construct(item[1:],base,idx)
            else:
                if base in record:
                    record[base].append(idx)
                else:
                    record[base]=[idx]
        for idx in range(len(puzzles)):
            puzzle=puzzles[idx]
            base=masks[puzzle[0]]
            construct(puzzle[1:],base,idx)
        ret=[0]*len(puzzles)
        for word in words:
            cur=convert(word)
            if cur in record:
                for idx in record[cur]:
                    ret[idx]+=1
        return ret
x=Solution()
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
x.findNumOfValidWords(words,puzzles)