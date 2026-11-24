class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        charSet = set()
        maxLength = 0

        for char in s:
            while char in charSet:
                charSet.remove(s[start])
                start += 1
            
            charSet.add(char)
            maxLength = max(maxLength, len(charSet))
        
        return maxLength
