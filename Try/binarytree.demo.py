from grid import Grid
from binary_tree import BinaryTree

# Create a grid of 5 rows and 10 columns
grid = Grid(5, 10)

# Apply the Binary Tree algorithm to generate the maze
BinaryTree.on(grid)

# Print the grid representation
print(grid)
