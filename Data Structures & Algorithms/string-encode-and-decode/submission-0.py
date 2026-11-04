class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ""
        spacer = "\n"

        for word in strs:
            encodedString += word
            encodedString += spacer
        
        return encodedString


    def decode(self, s: str) -> List[str]:

        return s.split("\n")[:-1]