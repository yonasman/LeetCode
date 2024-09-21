class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        hashMapT = {}
        hashMapS = {}
        minSteps = 0
        # build each hashmaps
        for c in s:
            hashMapS[c] = hashMapS.get(c,0) + 1
        for c in t:
            hashMapT[c] = hashMapT.get(c,0) + 1
        for key in hashMapS.keys():
            if key in hashMapT:
                minSteps += max(0, hashMapS[key] - hashMapT[key])
            else:
                minSteps += hashMapS[key]
        return minSteps