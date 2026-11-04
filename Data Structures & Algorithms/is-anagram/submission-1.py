class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charMap = defaultdict(int)
        for c in s: 
            charMap[c] += 1
        
        for c in t: 
            charMap[c] -= 1
        
        for c, count in charMap.items():
            if count != 0:
                return False
        
        return True
