class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # We calculate the length, convert it to a string, 
            # and stitch it together with the '#' and the word itself.
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Step 1: Send the scout 'j' forward to find the separator
            j = i
            while s[j] != '#':
                j += 1
                
            # Step 2: Extract the number and turn it into an integer
            length = int(s[i:j])
            
            # Step 3: Extract the word using the exact length boundary
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Step 4: Reset the anchor 'i' to the exact start of the next block
            i = j + 1 + length
            
        return res




        

