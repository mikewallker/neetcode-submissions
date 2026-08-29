class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # gimana klo string kosong
        sortedS = sorted(s)
        sortedT = sorted(t)
        if len(s) == len(t):
            for i in range(len(s)):
                if sortedS[i] != sortedT[i]:
                    return False
        else:
            return False

        return True