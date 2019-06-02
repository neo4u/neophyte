class Solution {
    public boolean isNStraightHand(int[] hand, int W) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for(int i : hand){
            minHeap.add(i);
        }
        while(minHeap.size() != 0) {
            int start = minHeap.poll();
            for(int j = 1; j < W; j++){
                if(minHeap.remove(start + j)) {
                    continue;
                }
                else {
                    return false;
                }
            }
        }
        return true;
    }
}