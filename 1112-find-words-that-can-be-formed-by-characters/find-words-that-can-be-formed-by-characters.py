from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        count = 0

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] <= chars_count.get(c,0) for c in word):
                count += len(word)
        return count




   
                        

                                    
                                                              
                                                     

                                                                                  

                               
                                                                                                          
