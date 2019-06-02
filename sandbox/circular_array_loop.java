public class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                continue;
            }
            // slow/fast pointer
            int slow = i, fast = getIndex(i, nums);
            while (nums[fast] * nums[i] > 0 && nums[getIndex(fast, nums)] * nums[i] > 0) {
                if (slow == fast) {
                    // check for loop with only one element
                    if (slow == getIndex(slow, nums)) {
                        break;
                    }
                    return true;
                }
                slow = getIndex(slow, nums);
                fast = getIndex(getIndex(fast, nums), nums);
            }
            // loop not found, set all element along the way to 0
            slow = i;
            int val = nums[i];
            while (nums[slow] * val > 0) {
                int next = getIndex(slow, nums);
                nums[slow] = 0;
                slow = next;
            }
        }
        return false;
    }
    
    public int getIndex(int i, int[] nums) {
        int n = nums.length;
        return i + nums[i] >= 0? (i + nums[i]) % n: n + ((i + nums[i]) % n);
    }
}