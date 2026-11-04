class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charMap = defaultdict(int)

        for char in s:
            charMap[char] += 1
        
        for char in t:
            charMap[char] -= 1
        
        for _char, count in charMap.items():
            if count != 0:
                return False
        
        return True
        