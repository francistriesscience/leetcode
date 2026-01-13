class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        min_level = 0
        current_level = 1
        
        queue = deque([root])

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                min_level = current_level
            
            current_level += 1
            
        return min_level
