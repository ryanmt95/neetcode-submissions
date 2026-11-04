class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for string in strs:
            charCount = defaultdict(int)

            for char in string: 
                charCount[char] += 1
            
            charCount = [(char, count) for char, count in charCount.items()]
            charCount.sort()

            stringKey = "".join([f"{char}{count}" for char, count in charCount])

            hashMap[stringKey].append(string)
        
        return list(hashMap.values())