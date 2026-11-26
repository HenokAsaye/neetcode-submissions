class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_cons = 1 if nums else 0
        i=0
        count = 1
        while i < len(nums)-1:
            if(nums[i+1] - nums[i] == 1):
                count +=1
                max_cons = max(max_cons,count)
            elif(nums[i+1] - nums[i] == 0):
                i+=1
                continue
            else:
                count = 1
            i+=1 
        return max_cons

        


        