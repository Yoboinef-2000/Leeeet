class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        # closestSum = float('inf')

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             currentSum = nums[i] + nums[j] + nums[k]
        #             if abs(currentSum - target) < abs(closestSum - target):
        #                 closestSum = currentSum

        # return closestSum

        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum

                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                else:
                    return currentSum

        return closestSum

