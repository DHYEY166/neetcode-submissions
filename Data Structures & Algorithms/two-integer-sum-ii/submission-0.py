class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        des = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if des[diff]:
                return [des[diff], i+1]
            des[numbers[i]] = i+1
        return []