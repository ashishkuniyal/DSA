class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float("inf")

        n = len(nums)

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                current = nums[i] + nums[left] + nums[right]

                
                if abs(current - target) < abs(closest - target):
                    closest = current

             
                if current == target:
                    return current

           
                elif current < target:
                    left += 1

              
                else:
                    right -= 1

        return closest
        