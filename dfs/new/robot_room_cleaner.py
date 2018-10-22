class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())
    
    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))
        
        for k in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y

            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                
                # Two moves to face the direction we came from
                robot.turnLeft() 
                robot.turnLeft()
                
                # Go back to the previous position
                robot.move()

                # Reset direction to what it was orginally
                robot.turnLeft()
                robot.turnLeft()

            # if neighbours were cleaned or unreachable keep turning and exploring new cells
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x

# For better understanding
# left, up, right, down
DIR = (
    (0, -1),    # Left
    (-1, 0),    # Up
    (0, 1),     # Right
    (1, 0)      # Down
)

class Solution2(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # assume we start at (0, 0) the origin
        self.dfs(robot, (0, 0), set(), 1)
        
    def dfs(self, robot, curr_pos, visited, facing_direction):
        robot.clean()
        visited.add(curr_pos)

        for i in range(4):
            robot.turnLeft()
            # for i in [0, 3], i+1 means how many times we have turned left
            # (facing_direction-(i+1))%4 therefore, is our new facing direction
            new_direction = (facing_direction - i - 1) % 4
            new_pos = (curr_pos[0] + DIR[new_direction][0], curr_pos[1] + DIR[new_direction][1])
            if new_pos not in visited and robot.move():
                self.dfs(robot=robot, curr_pos=new_pos, visited=visited, facing_direction=new_direction)
                # turn around
                robot.turnLeft()
                robot.turnLeft()
                # move back
                robot.move()
                # face the previous direction, such that we can continue turning left
                robot.turnLeft()
                robot.turnLeft()




# Example
# Initially:
# x, y = 0, 0
# dir_x, dir_y = 0, 1
# we visit 0, 1, if not visited and then
#   x, y = 0, 1
#   x, y = 0, 1
# else if 0,1 was visited,
#   dir_x, dir_y = -1, 0


# 1. Explanation
# To track the cells the robot has cleaned, start a index pair (i, j) from (0, 0). When go up, i-1; go down, i+1; go left, j-1; go right: j+1.

# 2. Explanation Detailed.
# We want to do a DFS with backtracking.
# The following details are different in this problem than a common dfs problem:
# 1. A way to encode already visited positions
#    (The easy solution is just use relative positions from the starting point)
# 2. A way to backtrack (The concept is the same,
#    we want to reset the position to what it originally was.
#    In this case the direction is also added in,
#    so we want to reset the direction it's facing to the
#    direction it originally was facing with the original position).

# The algorithm starts off at 0,0 which is our starting point
# (the boards starting point doesn't matter,
# and it doesn't matter that there are negative positions),
# as long as all the values are consistent.
# We add this position to our visited list and clean it. For each of the 4 directions,
# we calculate its next row and next column
# (remember that we are currently facing in the last direction moved,
# in this code's case the variable curDirection) if we went in that direction.
# If the next position is unvisited we try moving there.
# If we are able to move we call it recursively down the next branch.
# Essentially once we turn we try going down that direction for as deep as possible.
# If not, turn and keep going as deep as possible. So on, till no unvisited cells

# After we return from the recursive call we need to backtrack:
#                 robot.turnLeft();
#                 robot.turnLeft();
#                 robot.move();
#                 robot.turnRight();
#                 robot.turnRight();
# or we can use 2 turnLeft()s like I did.
# We reset the state by turning 180 degrees, moving, and then changing the direction back to what it originally was by turning another 180 degrees.
# Then we try the next direction (turning it to the right). After all 4 directions are tried it is automatically turned to the original direction after the loop since we turned right 4 times.

