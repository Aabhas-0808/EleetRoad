"""
Problem: Binary Search
Link: https://leetcode.com/problems/binary-search/

Summary:
Given a sorted array of integers and a target value, return the index of the target if found,
otherwise return -1.

Approach:
Use binary search algorithm. Compare target with middle element and eliminate half of the search space
in each iteration. If target is less than middle, search left half; if greater, search right half.
Continue until target is found or search space is empty.

Time Complexity: O(log n) - halve the search space in each iteration
Space Complexity: O(1) - only use constant extra space
"""

def binary_search(nums, target):
    """
    Perform binary search to find target in sorted array.
    Returns index of target or -1 if not found.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], -5) == -1
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([], 1) == -1
    
    print("All test cases passed!")
