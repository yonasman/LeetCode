class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = Counter(s)

        for index,value in enumerate(s):
            if char_counter[value] == 1:
                return index
        return -1
