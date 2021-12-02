# Description #
# Given: 
# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
        
# Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.
# Return empty list if root is None.

# Example 1 - following tree:
#                 2
#             8        9
#           1  3     4   5
        
# Should return following list:
# [2,8,9,1,3,4,5]


def tree_by_levels(node):
    res, stack = [], []
    if node:
        stack.append(node)
    while stack:
        curr = stack.pop(0)
        res.append(curr.value)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return res
