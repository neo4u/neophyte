from pprint import pprint

class Point():
    ''' Point class to store x and y coordinates, x is row number and y column number '''
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "x: "+str(self.x)+", y: "+str(self.y)
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self.__eq__(other)

class Matrix():
    def __init__(self):
        self.matrix = []

    def displayMatrix(self):
        ''' This function can be used display the matrix '''
        pprint(self.matrix)

    def checkIfPointExists(self, point):
        ''' This function can be used to check if a point lie in matrix '''
        row = len(self.matrix)
        col = len(self.matrix[0])
        return (point.x >= 0 and point.x < row and point.y >= 0 and point.y <col)

    def getValueAtPoint(self, point):
        ''' This function can be used to get the value at a point in matrix '''
        if self.checkIfPointExists(point):
            return self.matrix[point.x][point.y]
        else:
            return None

    def getNeighbors(self, point):
        ''' This function can be used to get the neighbors of a point '''
        neighbors = []
        if self.checkIfPointExists(Point(point.x,point.y-1)):
            neighbors.append(Point(point.x,point.y-1))
        if self.checkIfPointExists(Point(point.x,point.y+1)):
            neighbors.append(Point(point.x,point.y+1))
        if self.checkIfPointExists(Point(point.x-1,point.y)):
            neighbors.append(Point(point.x-1,point.y))
        if self.checkIfPointExists(Point(point.x+1,point.y)):
            neighbors.append(Point(point.x+1,point.y))
        return neighbors

    def updateValueByPoint(self, point, value):
        ''' This function can be used update data for a point in matrix '''
        if self.checkIfPointExists(point):
            self.matrix[point.x][point.y] = value

    def markShortestPath(self, source, destination, count='0'):
        ''' This function will update the distance in the matrix'''
        if source == destination:
            if self.getValueAtPoint(source) == 'o' or int(self.getValueAtPoint(source)) > int(count):
                self.updateValueByPoint(source, count)
            return
        elif self.getValueAtPoint(source) == 'w':
            return
        elif self.getValueAtPoint(source) == 'o' or int(self.getValueAtPoint(source)) > int(count):
            self.updateValueByPoint(source, count)
            neighbors = self.neighbors(source)
            for neighbor in neighbors:
                self.markShortestPath(neighbor, destination, str(int(count)+1))
            return

    def getShortestPath(self, source, destination):
        ''' This function assumes that markShortestPath has already been called '''
        path = []
        while source != destination:
            path.append(destination)
            neighbors = self.neighbors(destination)
            for neighbor in neighbors:
                if self.getValueAtPoint(neighbor) not in ['o','w'] and int(self.getValueAtPoint(neighbor)) == int(self.getValueAtPoint(destination))-1:
                    destination = neighbor
                    break
        path.append(destination)
        return reversed(path)

if __name__=="__main__":
    matrixObj = Matrix()
    ''' w is used for 1 and o for 0 '''
    matrixObj.matrix = [['w','w','w','o','o','w','o'],
                        ['w','o','o','o','o','w','o'],
                        ['w','o','w','w','w','w','o'],
                        ['w','o','o','o','o','o','o'],
                        ['w','w','w','w','w','w','w']]
    startPoint = Point(0,3)
    endPoint = Point(0,6)
    print("Input matrix")
    matrixObj.displayMatrix()
    print("Start point:",startPoint)
    print("End point:",endPoint)
    matrixObj.markShortestPath(startPoint, endPoint)
    print("Inplace path updation in matrix")
    matrixObj.displayMatrix()
    print("Shortest path is", matrixObj.getValueAtPoint(endPoint))
    print("Path from start to end")
    for point in matrixObj.getShortestPath(startPoint, endPoint):
        print(point)
