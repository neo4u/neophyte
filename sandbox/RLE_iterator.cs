/* public class RLEIterator
{
    private int[] nums;
    private int index;
    private int number;
    private int available;

    public RLEIterator(int[] A)
    {
        nums = A;
        index = 0;
        number = 0;
        available = 0;
    }s

    public int Next(int n)
    {
        while (index < nums.Length || available >= n)
        {
            if (available >= n)
            {
                available -= n;
                return number;
            }
            else
            {
                n -= available;
                available = nums[index];
                number = nums[index + 1];
                index += 2;
            }
        }

        available = 0;
        return -1;
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(A);
 * int param_1 = obj.Next(n);
 */
 */