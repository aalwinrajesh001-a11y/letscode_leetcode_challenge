class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s=0
        n=len(nums)
        for i in range(n):
            if i.bit_count()==k:
                s+=nums[i]
        return s
