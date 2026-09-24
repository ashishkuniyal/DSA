class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num=nums[i]
            digit_sum=sum(map(int,str(num)))
            if digit_sum==i:
                return i
        return -1
        