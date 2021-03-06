from abc import ABC, abstractmethod
import time


def sort_duration(sort_algorithms):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        sorted_nums = sort_algorithms(*args, **kwargs)
        end = time.time()
        total_time = end - start_time
        return [total_time, sorted_nums]
    return wrapper


class SortNums(ABC):

    @abstractmethod
    def __make_sort(self, nums):
        pass


class BubbleSort(SortNums):

    @sort_duration
    def _SortNums__make_sort(self, pf, nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        return nums


class InsertionSort(SortNums):

    @sort_duration
    def _SortNums__make_sort(self, pf, nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
        return nums


class MergeSort(SortNums):

    @sort_duration
    def _SortNums__make_sort(self, pf, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            lefthalf = nums[:mid]
            righthalf = nums[mid:]
            self._SortNums__make_sort(pf, lefthalf)
            self._SortNums__make_sort(pf, righthalf)
            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    nums[k] = lefthalf[i]
                    i = i + 1
                else:
                    nums[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                nums[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                nums[k] = righthalf[j]
                j = j + 1
                k = k + 1
        return nums


class SelectionSort(SortNums):

    @sort_duration
    def _SortNums__make_sort(self, pf, nums):
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        return nums
