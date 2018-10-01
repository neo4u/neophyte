class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        def getCoordinates(board,num):
            for i in [0,1]:
                for j in [0,1,2]:
                    if board[i][j]==num: return (i,j)

        def isValid(i,j):
            return i>=0 and i<=1 and j>=0 and j<=2

        def isWinPosition(board):
            if board[0][0]==1 and board[0][1]==2 and board[0][2]==3 and board[1][0]==4 and board[1][1]==5: return True
            return False

        self.nextMove=[(0,1),(0,-1),(1,0),(-1,0)]
        self.minSteps=20

        def puzzle(board,steps,i,j,previ,prevj):
                ## Max depth to be explored is set to 18
                if steps>18 or self.minSteps < steps: return
                elif i==1 and j==2 and isWinPosition(board): self.minSteps=min(self.minSteps,steps)
                else:
                    for a,b in self.nextMove:
                        newi,newj=i+a,i+b
                        if isValid(newi,newj) and (newi,newj)!=(previ,prevj):
                            board[newi][newj],board[i][j]=board[i][j],board[newi][newj]
                            puzzle(board,steps+1,newi,newj,i,j)
                            board[newi][newj],board[i][j]=board[i][j],board[newi][newj]

        x,y=getCoordinates(board,0)
        puzzle(board,0,x,y,-1,-1)

        return self.minSteps if self.minSteps<20 else -1