''' Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = { }
        for i in range(len(nums)):
            a = nums[i]
            if a in c:
                c[a]+=1
            else:
                c[a]=1
        sorted_elements = sorted(c, key=c.get, reverse=True)
        return sorted_elements[:k]
