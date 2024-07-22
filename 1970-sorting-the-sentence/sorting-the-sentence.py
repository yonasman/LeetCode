class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        # sort using the number at last         
        sorted_words = sorted(words, key = lambda x: int(x[-1]))
        # remove the last number         
        cleaned_words = [word[:-1] for word in sorted_words]
        return " ".join(cleaned_words)