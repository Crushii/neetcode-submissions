from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        return [key for key , value in count_dict.items() if value in sorted(count_dict.values(),reverse=True)[:k]]
        