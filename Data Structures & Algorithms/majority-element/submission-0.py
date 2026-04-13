class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore
        count = 0
        curr = 0

        for i in nums:
            if count == 0:
                curr = i
            
            if i == curr:
                count +=1
            else:
                count -=1
        return curr