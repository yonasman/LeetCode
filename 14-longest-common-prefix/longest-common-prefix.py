class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # set prefix to first string
        prefix = strs[0]
        for str in strs[1:]:
            while not str.startswith(prefix):
                # reduce the prefix by one last char
                prefix = prefix[:-1]
                # if prefix become empty return ""
                if not prefix:
                    return ""
        return prefix