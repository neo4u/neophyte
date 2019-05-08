public class Solution {
    public bool CanJump(int[] nums)
    {
        int lastGood = nums.Length - 1;

        for (int i = nums.Length - 1; i >= 0; i--)
        {
            if (i + nums[i] >= lastGood)
            {
                lastGood = i;
            }
        }

        return lastGood == 0;
    }
}