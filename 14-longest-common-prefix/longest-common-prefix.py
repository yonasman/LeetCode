class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n = len(strs)
        for i in range(len(strs[0])):
            prefix = strs[0][i]
            for j in range(n):
                if i >= len(strs[j]) or strs[j][i] != prefix:
                    return strs[0][:i]
        return strs[0]