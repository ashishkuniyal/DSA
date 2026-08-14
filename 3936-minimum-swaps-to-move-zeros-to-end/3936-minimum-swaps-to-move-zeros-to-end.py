class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zeros=nums.count(0)
        swaps=0
        for i in range(len(nums)-zeros):
            if nums[i]==0:
                swaps+=1
       
        return swaps
        