import random

class BinaryTree:
    #staticmethod
    def on(grid):
        for row in grid.grid:
            for cell in row:
                neighbors = []
                if cell.north:
                    neighbors.append(cell.north)
                if cell.east:
                    neighbors.append(cell.east)
                
                # Select a random neighbor
                neighbor = random.choice(neighbors) if neighbors else None
                
                # Link the cell to the chosen neighbor
                if neighbor:
                    cell.link(neighbor)

        return grid