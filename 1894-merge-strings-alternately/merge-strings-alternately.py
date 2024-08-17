class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        mergedString = ""
        for i in range(min(n1,n2)):
            mergedString += word1[i]
            mergedString += word2[i]
        if(n2 > n1):
            mergedString += word2[n1:]
        elif n1 > n2:
            mergedString += word1[n2:]
        return mergedString