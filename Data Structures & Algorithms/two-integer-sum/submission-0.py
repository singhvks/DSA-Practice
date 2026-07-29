class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        output = []
        for i in range(0,size):
            if len(output) > 0:
                break
            for j in range(0,size):
                if i == j:
                    pass
                elif nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    break
                else:
                    pass
        return output
        