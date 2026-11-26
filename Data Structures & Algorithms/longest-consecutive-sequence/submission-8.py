class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_cons = 1 if nums else 0
        for num in my_set:
            if num - 1 not in my_set:
                count = 1
                while num + 1 in my_set:
                    count += 1
                    num += 1
                max_cons = max(max_cons, count)

        return max_cons