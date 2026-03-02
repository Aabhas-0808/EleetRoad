"""
Problem: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/

Summary:
Reverse a singly linked list in-place and return the new head.

Approach:
Iterate through the list, reversing the direction of each node's pointer.
Use three pointers: prev (starts as None), current (starts as head), and next (temp storage).
For each node, save the next node, reverse the current node's pointer to prev, then move forward.

Time Complexity: O(n) - visit each node once
Space Complexity: O(1) - only use constant extra space

Alternative: Recursive approach also works but uses O(n) space for call stack.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    Reverse a singly linked list iteratively.
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def list_to_array(head):
    """Helper function to convert linked list to array for testing."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr):
    """Helper function to convert array to linked list for testing."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    head = array_to_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == [5, 4, 3, 2, 1]
    
    head = array_to_list([1, 2])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == [2, 1]
    
    head = array_to_list([1])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == [1]
    
    head = array_to_list([])
    reversed_head = reverse_list(head)
    assert list_to_array(reversed_head) == []
    
    print("All test cases passed!")
