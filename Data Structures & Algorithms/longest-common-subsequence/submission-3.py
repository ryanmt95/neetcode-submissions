class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memoisation = {}
        def search(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in memoisation:
                return memoisation[(i, j)]
            
            if text1[i] == text2[j]:
                subsequenceLength = 1 + search(i+1, j+1)
            else: 
                subsequenceLength = max(search(i+1, j), search(i, j+1))

            memoisation[(i, j)] = subsequenceLength
            return subsequenceLength
        
        return search(0, 0)

