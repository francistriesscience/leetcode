class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None
            
            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)
            
            if left_height > right_height:
                return left_height + 1, left_lca
            elif right_height > left_height:
                return right_height + 1, right_lca
            else:
                return left_height + 1, node
        
        _, lca = dfs(root)
        return lca
