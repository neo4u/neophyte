// The Image above represents the following
// All these are for the input array [-2,0,3,-5,2,-1]
// The inout array and the 0 based index ( highlighted in yellow ) are shown.

// Idea is to represent this array in a n*n matrix where n is the size of the initial array.

// There are 2 ways of doing this representation. Table 1 show one way
// In Table 1 , note the following

// Diagonal represents the original array. so arr[i][j] = nuts[i]

// The values in the next column come from the previous column
// row 0, col 0 = Since there is no column before it, nothing to do
// row 1, col 1 = This is a diagonal, so we already know its value
// row 0, col 1 = row 0 , col 0 + row 1, col1

// row 2, col 2 = Diagonal value , so its same as nums[2]
// row 1, col2 = row1,col1 + row2,col2
// row 0,col 2 = row0, col2 + row2, col2

// You get the idea

// Here is the code.

class NumArray {
    private int[][] ints;
    public NumArray(int[] nums) {
        ints = new int[nums.length][nums.length];
        populate(nums);
    }

    private void populate(int[] nums){
        for (int i=0; i < nums.length; i++){
            ints[i][i] = nums[i];

            for (int j= i-1; j >=0; j--){
                ints[j][i] = ints[j][i-1] + ints[i][i];
            }
        }
    }

    public int sumRange(int i, int j) {
        return ints[i][j];
    }
}
// The issue is that this uses n*n matrix space and its still a O(n2) due to initial population of array

// But, the idea to expand the problem to get a better understanding. Thats how the mind works, right ;)

// Key thing to notice above are these things

// The table was build from the fact the diagonal has the same values as the input array.
// The table was build bottom up, as in, from the diagonal value to the rows above it and this was done for each column.
// After the n*n matrix is build, take a look at the first row. It sure looks like a cumulative array. Nice!! Now knowing this , we can start to optimize the solution.
// Next, lets look at TABLE 2
// Based on the discoveries of TABLE1 , we use those to build table 2

// We know that if we can get a cumulative array , represented by first row, then the rest of the table can be build.
// To build from row 0 to all the other rows, we would have to go top ( row 0 ) to bottom. Do this for every column, like it was done in TABLE 1
// The last column in the table shows the example, which follows the following rule

// row0 - represents the cumulative array , lets call it cArr

// val(i,j) = cArr(j) - cArr(i)

// Thats it, this means, that there is no need to build a n*n array if we know the cumulative Array

// Now the code is easy

public class NumArray {
    int[] nums;

    public NumArray(int[] nums) {
        for(int i = 1; i < nums.length; i++)
            nums[i] += nums[i - 1];
        
        this.nums = nums;
    }

    public int sumRange(int i, int j) {
        if(i == 0)
            return nums[j];
        
        return nums[j] - nums[i - 1];
    }
}

// I have seen a lot of people post a similar solution for this problem, and they look like geniuses. I spend about 4 hours on this problem from start to finish. Thats a long time and with this article I want to say that, it does take time, initially. So if you are seeing this problem or similar problems and its taking you time to come up with a solution, its ok. Take you time, because with that time, your wirings in the brain are also changing and that change is slow and long process.
// Second point I want to make is that, when solving problems like these, expand the problem, even if expansion of the problem is using extra space along with additional time. So expansion of a problem is causing both Time And Space complexity to increase. ... And thats Ok, because with the expansion of the problem, you will discover new things , and you can build on top of those new things a optimal solution. This type of thinking process goes a long way during interviews.
// Imagine if you got this problem during Google interview. If you start by expanding the problem ... which atleast solves the problem and then you optimize it. I say, you are hired.