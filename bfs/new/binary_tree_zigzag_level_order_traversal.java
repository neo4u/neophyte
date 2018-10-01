// Here is mine BFS solution

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        
        if(root == null) {
            return result;
        }
        
        queue.add(root);
        
        while(!queue.isEmpty()) {
            int nodes = queue.size();
            List<Integer> levelNodes = new ArrayList<>();
            
            for(int i = 0; i < nodes; i++) {
                TreeNode current = queue.poll();

                if(result.size() % 2 == 0) {
                    levelNodes.add(current.val);   
                }
                else {
                    levelNodes.add(0, current.val);
                }
                                
                if(current.left != null) {
                    queue.add(current.left);
                }

                if(current.right != null) {
                    queue.add(current.right);
                }
            }
            result.add(levelNodes);
        }
        return result;
     }
}