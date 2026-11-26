class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            my_dict[num] = True
        max_cons = 1 if nums else 0
        count = 1
        for num in my_dict:
            if num-1 not in my_dict:
                while num+1 in my_dict:
                    count +=1
                    num +=1
                max_cons = max(max_cons,count)
                count = 1
        return max_cons
                        


        


        