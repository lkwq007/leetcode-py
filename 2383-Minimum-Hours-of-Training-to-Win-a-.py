class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy=max(sum(energy)+1-initialEnergy,0)
        ret=energy
        acc=initialExperience
        for item in experience:
            if acc<=item:
                ret+=item-acc+1
                acc=item+1
            acc+=item
        return ret
