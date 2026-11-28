class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        i=0
        j=len(nums)-1
        while i<j:
            if (nums[i]+nums[j] > target):
                j-=1
            elif (nums[i]+nums[j] < target):
                i+=1
            else:
                break
        ans.append(i+1)
        ans.append(j+1)

        return ans