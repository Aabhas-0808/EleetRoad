"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Summary:
Given a string containing characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if brackets are closed in the correct order.

Approach:
Use a stack to track opening brackets. When we encounter a closing bracket, check if it matches
the most recent opening bracket (top of stack). If all brackets match and stack is empty at the end,
the string is valid.

Time Complexity: O(n) - single pass through string
Space Complexity: O(n) - stack can store up to n/2 opening brackets
"""

def is_valid(s):
    """
    Check if parentheses in string are valid.
    """
    if len(s) % 2 != 0:
        return False
    
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack) == 0


if __name__ == "__main__":
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("") == True
    assert is_valid("((") == False
    assert is_valid("))") == False
    
    print("All test cases passed!")
