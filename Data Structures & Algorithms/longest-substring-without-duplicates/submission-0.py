class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        charSet = set()
        maxLength = 0

        for index, char in enumerate(s):
            if char in charSet:
                while s[start] != char:
                    charSet.remove(s[start])
                    start += 1
                
                start += 1
            
            else:
            
                charSet.add(char)
                maxLength = max(maxLength, len(charSet))
        
        return maxLength
