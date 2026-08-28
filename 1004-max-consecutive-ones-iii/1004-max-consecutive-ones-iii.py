class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        max_w=0
        nums_zeroes=0
        for r in range(n):
            if nums[r]==0:
                nums_zeroes+=1
            while nums_zeroes>k:
                if nums[l]==0:
                    nums_zeroes-=1
                l+=1
            w=r-l+1
            max_w=max(max_w,w)
        return max_w
        