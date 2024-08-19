class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = {}
        for letter in s:
            if letter in seen:
                return letter
            seen[letter] = 1
            