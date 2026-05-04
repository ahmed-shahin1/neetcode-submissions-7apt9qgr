class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers)
        while left < right:
            if numbers[left] + numbers[right - 1] > target:
                right -=1
            elif numbers[left] + numbers[right - 1] < target:
                left +=1
            else:
                return [left + 1, right]
                      