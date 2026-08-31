class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = 0
        max_index = 0

        for i in range(n):
            if nums[i] < nums[min_index]:
                min_index = i

            if nums[i] > nums[max_index]:
                max_index = i

        a = min(min_index, max_index)
        b = max(min_index, max_index)

        front = b + 1
        back = n - a
        both = (a + 1) + (n - b)

        return min(front, back, both)