"""
This is the robot's control interface.
You should not implement it, or speculate about its implementation
"""
class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """
        pass

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """
        pass

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """
        pass


class Solution:
    def cleanRoom(self, robot: Robot) -> None:
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])
                if not new_cell in visited and robot.move():
                    dfs(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        dfs()


class Solution:
    def cleanRoom(self, robot: 'Robot') -> None:
        visited = set()
        self.dfs(robot, 0, 0, visited)

    def go_up(self, robot: 'Robot') -> bool:
        success = robot.move()
        return success

    def go_left(self, robot: 'Robot') -> bool:
        robot.turnLeft()
        success = robot.move()
        robot.turnRight()
        return success

    def go_right(self, robot: 'Robot') -> bool:
        robot.turnRight()
        success = robot.move()
        robot.turnLeft()
        return success

    def go_down(self, robot: 'Robot') -> bool:
        robot.turnLeft()
        robot.turnLeft()
        success = robot.move()
        robot.turnRight()
        robot.turnRight()
        return success

    def dfs(self, robot, i, j, visited):
        robot.clean()
        visited.add((i, j))

        if (i - 1, j) not in visited:
            if self.go_up(robot):
                self.dfs(robot, i - 1, j, visited)
                self.go_down(robot)

        if (i + 1, j) not in visited:
            if self.go_down(robot):
                self.dfs(robot, i + 1, j, visited)
                self.go_up(robot)

        if (i, j - 1) not in visited:
            if self.go_left(robot):
                self.dfs(robot, i, j - 1, visited)
                self.go_right(robot)

        if (i, j + 1) not in visited:
            if self.go_right(robot):
                self.dfs(robot, i, j + 1, visited)
                self.go_left(robot)


# 489. Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/description/
