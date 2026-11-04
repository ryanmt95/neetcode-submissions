class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for word in strs: 
            charCount = [0] * 26

            for c in word: 
                charCount[ord(c) - 97] += 1
            
            key = ''
            for index, count in enumerate(charCount):
                if count > 0: 
                    key += f'{chr(index + 97)}{count}'
            
            anagramMap[key].append(word)
        
        return list(anagramMap.values())
