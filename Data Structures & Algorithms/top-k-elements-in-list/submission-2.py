class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(),key=lambda items:items[1],reverse=True))
        ans= []
        for i,j in sorted_count.items():
            ans.append(i)
        return ans[:k]