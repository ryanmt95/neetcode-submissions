class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = defaultdict(list)

        for word in strs:
            charMap = [0 for _ in range(26)]

            for char in word: 
                letterIndex = ord(char) - ord('a')
                charMap[letterIndex] += 1
            
            anagramMap[tuple(charMap)].append(word)

        return list(anagramMap.values())
