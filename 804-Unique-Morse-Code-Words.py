class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        record={}
        base=ord("a")
        total=0
        for word in words:
            code=""
            for c in word:
                code+=morse[ord(c)-base]
            if code not in record:
                record[code]=0
                total+=1
        return total