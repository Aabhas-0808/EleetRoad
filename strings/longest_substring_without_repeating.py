"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Summary:
Find the length of the longest substring without repeating characters in a given string.

Approach:
Use sliding window technique with a hash map to track character positions.
Expand the window by moving right pointer, and shrink it from left when we encounter a duplicate.
Track the maximum window size seen.

Time Complexity: O(n) - each character visited at most twice (once by right, once by left pointer)
Space Complexity: O(min(n, m)) - where m is charset size (at most 256 ASCII or 128 for basic ASCII)
"""

def length_of_longest_substring(s):
    """
    Find length of longest substring without repeating characters.
    """
    char_index = {}
    max_length = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abcdef") == 6
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring("dvdf") == 3
    
    print("All test cases passed!")
