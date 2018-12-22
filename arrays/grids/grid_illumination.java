public class LampIlluminationGrid {

    private static class Lamp{
        private int row;
        private int col;

        public Lamp(int row, int col){
            this.row = row;
            this.col = col;
        }
    }

    private boolean[][] grid;

    public LampIlluminationGrid(int n, Lamp[] lampsCoordinates){
        grid = new boolean[n][n];

        for(Lamp lamp : lampsCoordinates){
            int targetRow = lamp.row;
            int targetCol = lamp.col;

            // illuminate row.
            for(int c = 0; c < n; c++){
                grid[targetRow][c] = true;
            }

            // illuminate col
            for(int r = 0; r < n; r++){
                grid[r][targetCol] = true;
            }

            // illuminate diagonal.
            int r = targetRow;
            int c = targetCol;
            while(r >= 0 && c >=0){
                grid[r][c] = true;
                r--;
                c--;
            }
            r = targetRow;
            c = targetCol;
            while(r < n && c < n){
                grid[r][c] = true;
                r++;
                c++;
            }

            r = targetRow;
            c = targetCol;
            while(r >= 0 && c < n){
                grid[r][c] = true;
                r--;
                c++;
            }

            r = targetRow;
            c = targetCol;
            while (r < n && c >= 0){
                grid[r][c] = true;
                r++;
                c--;
            }
        }
    }

    public boolean isGridPointIlluminated(Lamp targetPoint){
        if(targetPoint == null || targetPoint.row < 0 || targetPoint.col < 0
                || targetPoint.row >= grid.length || targetPoint.col >= grid.length){
            throw new IllegalArgumentException();
        }
        return grid[targetPoint.row][targetPoint.col];
    }

    public static void main(String[] args) {
        Lamp[] lamps = {
            new Lamp(2, 1),
            new Lamp(2, 2)
        };
        int N = 5;
        LampIlluminationGrid lampIlluminationGrid = new LampIlluminationGrid(N, lamps);

        for(int row = 0; row < N; row++){
            System.out.println(Arrays.toString(lampIlluminationGrid.grid[row]));
        }

        Lamp target = new Lamp(0,1);
        System.out.println("targetPoint: " + lampIlluminationGrid.isGridPointIlluminated(target));
    }
}