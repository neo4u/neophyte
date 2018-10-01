public int maxSubArrayLen(int[] nums, int targetSum) {
    int sum = 0, max = 0;
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();

    for (int i = 0; i < nums.length; i++) {
        sum = sum + nums[i];

        if (sum == targetSum) {
            max = i + 1;
        } else if (map.containsKey(sum - targetSum)) {
            max = Math.max(max, i - map.get(sum - targetSum));
        }

        if (!map.containsKey(sum)) {
            map.put(sum, i);
        }
    }
    return max;
}
// The HashMap stores the sum of all elements before index i as key, and i as value.
// For each i, check not only the current sum but also (currentSum - previousSum) to see if there is any that equals k,
//and update max length.
// PS: An "else" is added. Thanks to beckychiu1988 for comment.