"""
Problem: Climbing Stairs
Link: https://leetcode.com/problems/climbing-stairs/

Summary:
You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps.
How many distinct ways can you reach the top?

Approach:
This is a Fibonacci sequence problem. To reach step n, you can come from step (n-1) or (n-2).
So ways[n] = ways[n-1] + ways[n-2]. Use dynamic programming to avoid recomputation.
We can optimize space by only storing the last two values instead of entire array.

Time Complexity: O(n) - compute result for each step once
Space Complexity: O(1) - only store two previous values
"""

def climb_stairs(n):
    """
    Calculate number of distinct ways to climb n stairs.
    """
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    
    print("All test cases passed!")
