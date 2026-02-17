class TreeNodes(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution(object):
    def countNodes(self, root):
        if root == None:
            return 0 
        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        return leftCount + rightCount + 1
        