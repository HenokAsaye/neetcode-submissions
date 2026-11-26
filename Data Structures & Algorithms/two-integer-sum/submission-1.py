class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = defaultdict(int)
        for i,j in enumerate(nums):
            if target-j in two_sum:
                return [two_sum[target-j],i]
            two_sum[j]=i
        

            
        