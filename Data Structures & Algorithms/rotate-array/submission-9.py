class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k %= length

        def reverse(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l,r = l + 1, r - 1
        
        reverse(0, length - 1)
        reverse(0 , k - 1)
        reverse(k, length - 1)
        
        