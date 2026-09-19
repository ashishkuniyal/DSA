class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            nums[i]=summ
        return nums
        