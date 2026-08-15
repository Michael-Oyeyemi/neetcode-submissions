class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unums = set(nums)
        highest = 0

        for num in range(len(nums)):
            if nums[num] - 1 not in unums:
                length = 1
                s = nums[num]
                while s+1 in unums:
                    s+=1
                    length += 1
                if length > highest:
                    highest = length
        return highest