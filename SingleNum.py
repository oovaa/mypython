def singleNumber(self, nums: list[int]) -> int:
    result = [i for i in nums if nums.count(i) == 1]
    return(result[0])
