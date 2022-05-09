"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        if not root:
            return ret
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ret.append(node.val)
            children = node.children[::-1]
            stack.extend(children)
        return ret
