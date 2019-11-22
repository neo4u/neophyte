class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1

        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            elif i == 'L': dx, dy = -dy, dx
            elif i == 'G': x, y = x + dx, y + dy

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)



# 1041. Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/description/

# There are only two scenarios where the robot can come back to its original location:

# the robot is already back to its origin by the end of the string traversal, and
# the robot is away from the origin, but heading to a direction different from its initial direction.
# For example, if the robot is facing left by the end of the first string traversal,
# after three other traversals of left->left->left, it is back to the origin.

# A second example is that if the robot is facing down by the end of the first string traversal,
# it only takes another traversal for it to get back to the origin.

# Another tip on how to change the directions.
# You actually do not need to keep a list of all possible directions [(0,1), (-1,0), (0,-1), (1,0)].
# Just swap dx and dy and add a negative sign to one of it to rotate the direction by 90 degrees.

# The proof is that the dot product of (dx,dy) and (dy,-dx) is 0,
# meaning that these two vectors are perpendicular to each other.
