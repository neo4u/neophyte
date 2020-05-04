class Solution:
    def cleanRoom(self, robot: 'Robot') -> None:
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.visited = set()
        self.dfs(robot)

    def go_back(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def dfs(self, robot, cell=(0, 0), d=0):
        self.visited.add(cell)
        robot.clean()

        for i in range(4):
            new_d = (d + i) % 4
            new_cell = (cell[0] + self.dirs[new_d][0], cell[1] + self.dirs[new_d][1])

            if not new_cell in self.visited and robot.move():
                self.dfs(robot, new_cell, new_d)
                self.go_back(robot)

            # turn the robot following chosen direction : clockwise
            robot.turnRight()


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
