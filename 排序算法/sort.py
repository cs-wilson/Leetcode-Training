# 冒泡排序
def bubbleSort(nums: list):
    for i in range(len(nums)):
        for j in range(len(nums) - i -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]            
    return nums


# 选择排序
def selectionSort(nums: list):
    for i in range(len(nums) - 1):
        minIndex = i
        for j in range(i + 1,len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        if i != minIndex:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums

# 插入排序
def insertionSort(nums: list):
    for i in range(1, len(nums)):
        preIndex = i - 1
        current = nums[i]
        while preIndex >= 0 and nums[preIndex] > current:
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = current
    return nums

# 归并排序
def mergeSort(nums: list):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def merge(left: list, right: list):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop())
    while left:
        result.append(left.pop())
    while right:
        result.append(right.pop())
    return result

# 快速排序
def quickSort(nums: list):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left_nums = [i for i in nums[1:] if i <= pivot]
    right_nums = [i for i in nums[1:] if i > pivot]

    return quickSort(left_nums) + [pivot] + quickSort(right_nums)


nums = [61, 17, 29, 22, 34, 60, 72, 21, 50, 1, 62]
# print("bubbleSort", bubbleSort(nums))
# print("selectionSort", selectionSort(nums))
# print("insertionSort", insertionSort(nums))
print("mergeSort", mergeSort(nums))
# print("quickSort", quickSort(nums))