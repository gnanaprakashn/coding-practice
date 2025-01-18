''' Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.'''
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            # Sort the word to use as the dictionary key
            a = ''.join(sorted(word))
            
            # Add the word to the corresponding group
            if a in anagrams:
                anagrams[a].append(word)
            else:
                anagrams[a] = [word]
        
        # Collect and return all the anagram groups
        return list(anagrams.values())
