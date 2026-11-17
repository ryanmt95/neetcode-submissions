class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = defaultdict(list)

        for word in strs:
            charMap = [0 for _ in range(26)]

            for char in word: 
                letterIndex = ord(char) - ord('a')
                charMap[letterIndex] += 1

            charKey = ""
            for index, count in enumerate(charMap):
                if count > 0:
                    letter = chr(index + ord('a'))
                    charKey += f"{letter}{count}"
            
            anagramMap[charKey].append(word)

        return list(anagramMap.values())
