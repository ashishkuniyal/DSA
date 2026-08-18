class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k=k % len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        """
        Do not return anything, modify nums in-place instead.
        """
        