class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        s = s.lower()

        print(s)
        while left < right:

            while left < len(s) and not s[left].isalnum():
                left += 1
            
            while right > 0 and not s[right].isalnum():
                right -= 1
            
            if left < right and s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True