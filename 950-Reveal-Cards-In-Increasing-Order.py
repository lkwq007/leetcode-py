class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ret=[]
        total=len(deck)
        for idx in range(len(deck)):
            ret.append(deck[idx])
            if idx!=total-1:
                tmp=ret[0]
                ret.pop(0)
                ret.append(tmp)
        return ret[::-1]
