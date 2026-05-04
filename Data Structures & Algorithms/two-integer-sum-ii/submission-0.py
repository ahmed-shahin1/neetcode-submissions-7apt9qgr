class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list1 = len(numbers)
        total = 0
        for i in range(list1):
            for j in range(1, list1):
                total = numbers[i] + numbers[j]
                if numbers[i] < numbers[j] and total == target:
                    return [i+1,j+1]        