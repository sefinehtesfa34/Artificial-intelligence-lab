from queue import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        queue.append(root)
        if not root:
            return 
        output=[]
        while queue:
            size = len(queue)
            palindrome=[]
            for i in range(size):
                top=queue.popleft()
                if top.left:
                    queue.append(top.left)
                    palindrome.append(top.left.val)
                if top.right:
                    palindrome.append(top.right.val)
                    queue.append(top.right)
            if palindrome:
                output.append(palindrome)
        output.insert(0,[root.val])
        return output