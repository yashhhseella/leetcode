class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(nums) > len(list(set(nums))))

# just check if the length of the set of nums is less than the length of nums itself