// 9ms C++ iterative, concise code with explanation
// Using a queue mQ to perform level order traversal.
// In the beginning of a level traversal, the last element is pushed into result array ret.
// The core idea is similar with Binary Tree Level Order Traversal

// O(n) time, O(logn) space

class Solution {
public:
    vector<int> rightSideView(TreeNode *root) {
        queue<TreeNode*>mQ;
        vector<int> ret;
        if(!root)return ret;
        mQ.push(root);
        while(!mQ.empty()){
            ret.push_back(mQ.back()->val);
            for(int i=mQ.size();i>0;i--){
                TreeNode *tn=mQ.front();
                mQ.pop();
                if(tn->left)mQ.push(tn->left);
                if(tn->right)mQ.push(tn->right);
            }
        }
        return ret;
    }
};