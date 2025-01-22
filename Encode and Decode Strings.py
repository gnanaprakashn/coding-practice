''' Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode '''

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            #my logic is i get the each string thought the iteration and
            #i count the len of the string and place it in infront of string + hash for encode and add this in new variable
            res += str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #here i assingn the i and j for find the len of string and hash 
        while i< len(s):
            
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            #if we found the hash we get the len of string besides the len
            i = j+1
            j = length +i
            
            res.append(s[i:j])
            #by slicing we get the encode string 
            i=j
        return res
