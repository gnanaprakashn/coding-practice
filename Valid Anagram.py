''' Given two strings s and t, return true if the two strings are anagrams of each other,
otherwise return false. '''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            #my logic is i sorted the two words if its is equal it is anagrams othere not
            return sorted(s) == sorted(t)
            
