class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for str in s:
            dict1[str] = dict1.get(str,0) + 1
        for str in t:
            dict2[str] = dict2.get(str,0) + 1
        return dict1 == dict2