import Maze
def view(grid):
for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == EMPTY:
                print("  ", end = "")
                    
            elif grid[i][j] == WALL:
                print("##", end = "")
                    
            elif grid[i][j] == START:
                print("^^", end = "")
                    
            elif grid[i][j] == END:
                print("$$", end = "")
                    
            elif grid[i][j] == VISITED:
                print("..", end = "")
                    
            else:
                raise AssertionError
            
        print()

