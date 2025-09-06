def binarySearch(arr: list, target: int) -> list:
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


nums = [2, 5, 7, 10, 14, 20, 25]
result = binarySearch(nums, 20)
print(f"index:{result} = {nums[result]}")