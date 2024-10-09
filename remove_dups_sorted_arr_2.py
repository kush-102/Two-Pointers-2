class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        n = len(nums)
        k = 2

        while fast < n:
            if fast > 0 and nums[fast] == nums[fast - 1]:
                count += 1
            else:
                count = 1

            if count <= k:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

        # Time complexity is O(n)
        # space complexity is O(1)
