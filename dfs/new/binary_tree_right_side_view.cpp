// My first implementation is as follows, as you can see , my consideration loses some cases.
// When the right-sub-tree-sub-tree is NULL then MY Implementation can not return the correct results.

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        help(root, result);
        return result;
    }
    
    void help(TreeNode* root, vector<int>& result){
        if(!root)   return;
        result.push_back(root->val);
        if(root->right)   help(root->right, result);
        else if(root->left)  help(root->left, result);
        else return;
    }
};

// To fix this problem , I refered to others' posts, as you can see, I add a int-variable-to check the current
// level node whether has been added. IF not, just add it. IF added, then we can reject add the left-sub-
// tree-node by checking the level

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        help(root, result, 1);
        return result;
    }
    
    void help(TreeNode* root, vector<int>& result, int level){
        if(!root)   return;
        if(result.size() < level) result.push_back(root->val);
        help(root->right, result, level+1);
        help(root->left, result, level+1);
    }
};