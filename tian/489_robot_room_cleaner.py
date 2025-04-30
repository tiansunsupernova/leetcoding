# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def btrack(cell = (0, 0), d = 0):
            seen.add(cell)
            robot.clean()

            i, j = cell
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for k in range(4):
                new_d = (d + k) % 4
                x = i + dx[new_d]
                y = j + dy[new_d]
                new_cell = (x, y)

                if not new_cell in seen and robot.move():
                    btrack(new_cell, new_d)
                    back()
                robot.turnRight()

        seen = set()
        btrack()




            
        