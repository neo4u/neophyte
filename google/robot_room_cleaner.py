class Solution(object):       
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def dfs(cell = (0, 0), d = 0):
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
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_up():
            success = robot.move()
            return success

        def go_left():
            robot.turnLeft()
            success = robot.move()
            robot.turnRight()
            return success

        def go_right():
            robot.turnRight()
            success = robot.move()
            robot.turnLeft()
            return success

        def go_down():
            robot.turnLeft()
            robot.turnLeft()
            success = robot.move()
            robot.turnRight()
            robot.turnRight()
            return success

        def dfs(i, j):
            robot.clean()
            visited.add((i, j))
            if (i - 1, j) not in visited:
                if go_up():
                    dfs(i - 1, j)
                    go_down()
            if (i + 1, j) not in visited:
                if go_down():
                    dfs(i + 1, j)
                    go_up()
            if (i, j - 1) not in visited:
                if go_left():
                    dfs(i, j - 1)
                    go_right()
            if (i, j + 1) not in visited:
                if go_right():
                    dfs(i, j + 1)
                    go_left()

        visited = set()
        dfs(0, 0)
    