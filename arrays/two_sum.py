"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Summary:
Given an array of integers and a target sum, return indices of two numbers that add up to the target.

Approach:
Use a hash map to store each number and its index as we iterate through the array.
For each element, check if (target - current element) exists in the hash map.
If it exists, we found the pair. Otherwise, add current element to hash map.

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - hash map stores up to n elements
"""

def two_sum(nums, target):
    """
    Find two numbers in the array that sum to target.
    Returns indices of the two numbers.
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
    
    print("All test cases passed!")
