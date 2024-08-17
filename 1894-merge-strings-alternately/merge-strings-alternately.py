class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        s = ""
        if n1 < n2:
            min_len = n1
            max_len = n2
        else:
            min_len = n2
            max_len = n1
        for i in range(min_len):
            s += word1[i]
            s += word2[i]
        if(max_len == n2):
            for j in range(min_len,max_len):
                s += word2[j]
        elif max_len == n1:
            for j in range(min_len,max_len):
                s += word1[j]
        return s