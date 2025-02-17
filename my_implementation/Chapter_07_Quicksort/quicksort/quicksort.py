import random
from typing import List


def partition_wrong_version(arr: List, start: int, end: int) -> int:
    """
    This method is generated by AI, but I think it is wrong.
    arr[return_index] is not necessarily the pivot.
    
    TODO: But can we modify it to make it correct?

    Args:
        arr (List): the list to partition
        start (int): inclusive
        end (int): inclusive

    Returns:
        the pivot index
    """
    pivot_index = random.randint(start, end)
    pivot = arr[pivot_index]
    left = start
    right = end
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            # Maybe we don't need to update left and right here ???
            left += 1
            right -= 1
    return left


def partition(arr: List, start: int, end: int) -> int:
    """
    Args:
        arr (List): the list to partition
        start (int): inclusive
        end (int): inclusive
    Returns:
        the pivot index
    """
    pivot_index = random.randint(start, end)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= arr[end]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
            
            

def quicksort(arr: List, start: int, end: int):
    """

    Args:
        arr (List): the list to sort
        start (int): inclusive
        end (int): inclusive
    """
    if start >= end:
        return
    pivot_index = partition(arr, start, end)
    # pivot_index = partition_wrong_version(arr, start, end)
    quicksort(arr, start, pivot_index - 1)
    quicksort(arr, pivot_index + 1, end)
    
    
if __name__ == '__main__':
    import copy
    # arr = [12, 1, 100, 5, 9, 15]
    # arr_copy = copy.deepcopy(arr)
    # pivot_index = partition_wrong_version(arr, 0, len(arr) - 1)
    # print(arr, pivot_index)
    # pivot_index_002 = partition(arr_copy, 0, len(arr_copy) - 1)
    # print(arr_copy, pivot_index_002)
    
    
    for i in range(1, 1000):
        arr = [random.randint(-100, 100) for _ in range(i)]
        arr_copy = copy.deepcopy(arr)
        quicksort(arr, 0, len(arr) - 1)
        assert arr == sorted(arr_copy), f"arr: {arr}, arr_copy: {sorted(arr_copy)}"
    print("All tests passed!")