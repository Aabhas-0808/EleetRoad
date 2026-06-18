"""
Problem: Binary Tree Maximum Depth
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Summary:
Find the maximum depth of a binary tree (number of nodes along the longest path from root to leaf).

Approach:
Use recursive depth-first search. The depth of a tree is 1 + max(left subtree depth, right subtree depth).
Base case: empty tree has depth 0.

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion stack depth equals tree height (worst case O(n) for skewed tree)

Alternative: BFS with level-order traversal also works with O(w) space where w is max width.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """
    Find the maximum depth of a binary tree.
    """
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert max_depth(root) == 3
    
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert max_depth(root) == 2
    
    root = None
    assert max_depth(root) == 0
    
    root = TreeNode(1)
    assert max_depth(root) == 1
    
    print("All test cases passed!")
