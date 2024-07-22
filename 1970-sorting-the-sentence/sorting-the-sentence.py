class Solution:
    def sortSentence(self, s: str) -> str:
        str = s.split(" ")
        n = len(str)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if(int(str[j][-1]) > int(str[j + 1][-1])):
                    str[j],str[j+1] = str[j+1],str[j]
        str = [word[:-1] for word in str]
        return " ".join(str)