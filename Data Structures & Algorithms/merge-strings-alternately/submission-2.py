class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = ''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                n = n + word1[i]
            
            if i < len(word2):
                n = n + word2[i]
        return n


        