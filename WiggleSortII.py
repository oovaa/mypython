def wiggleSort(nums: list[int]) -> None:
    temx = None
    temn = None
    for i, v in enumerate(nums):
        temx = max(nums[i:])
        temn = min(nums[i:])
        print(i, temn, temx)


nums = [1, 5, 1, 1, 6, 4]
wiggleSort(nums)
print(nums)
