from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        for item in Counter(nums).most_common(k):
            res.append(item[0])
        return res