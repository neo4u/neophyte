class Solution {
public:
    int mem[100][100][100]; // initialized to 0, mem[left][right][k] means value from boxes[left]~boxes[right] followed by 
    // k same color boxes. Follow does not mean strictly consecutive boxes, for example, [1, 3, 2, 3, 4], 3 can be 
    // followed by the other 3 because we can remove 2 first
    
    int removeBoxes(vector<int>& boxes) {
        return DFS(boxes,0,boxes.size()-1,0);
    }
    
    int DFS(vector<int>& boxes, int l,int r,int k){
        if (l>r) return 0; 
        if (mem[l][r][k]) return mem[l][r][k]; // if we have calculated this DFS result, return it
        
        mem[l][r][k] = DFS(boxes,l,r-1,0) + (k+1)*(k+1); // box[l][r] result is box[l][r-1]+(k+1)^2
        for (int i=l; i<r; i++) // go through each box from left
            if (boxes[i]==boxes[r]) // check for same color box as boxes[r]
                mem[l][r][k] = max(mem[l][r][k], DFS(boxes,l,i,k+1) + DFS(boxes,i+1,r-1,0)); // if we found same color box,
                // then we have a chance to get a higher value by group boxes[l]~boxes[i] and boxes[r] together, plus the 
                // value from boxes[i+1]~boxes[r-1]
        return mem[l][r][k];
    }
};