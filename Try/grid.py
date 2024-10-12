from cell import Cell
import random

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        # RGB color components
        self.r = 214
        self.g = 220
        self.b = 230

        # Initialize grid with cells and configure neighbors
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        """Create a 2D list (grid) of Cell objects."""
        return [[Cell(row, column) for column in range(self.columns)] for row in range(self.rows)]

    def configure_cells(self):
        """Configure each cell with its neighbors."""
        for cell in self.each_cell():
            row, col = cell.row, cell.column
            cell.north = self[row-1, col] if row > 0 else None
            cell.south = self[row+1, col] if row < self.rows - 1 else None
            cell.west = self[row, col-1] if col > 0 else None
            cell.east = self[row, col+1] if col < self.columns - 1 else None
            cell.southeast = self[row+1, col+1] if (row < self.rows - 1 and col < self.columns - 1) else None


    def __getitem__(self, position):
        row, column = position
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.grid[row][column]
        return None

    def random_cell(self):
        """Get a random cell from the grid."""
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        return self[row, column]

    def size(self):
        """Return the total number of cells in the grid."""
        return self.rows * self.columns

    def each_row(self):
        """Yield each row in the grid."""
        for row in self.grid:
            yield row

    def each_cell(self):
        """Yield each cell in the grid."""
        for row in self.grid:
            for cell in row:
                yield cell

    def contents_of(self, cell):
        """Return the display content of a cell (currently empty)."""
        return " "

    def black_foreground(self):
        """Return an ANSI code for setting the foreground color to the RGB values."""
        return f"\033[38;2;{self.r};{self.g};{self.b}m"
   
    # def __str__(self):
    #     # Top border
    #     output = "\u250F"  # Top left corner
    #     for _ in range(self.columns):
    #         output += "\u2501\u2501\u2501"  # Horizontal lines for top
    #     output += "\u2513\n"  # Top right corner

    #     for row in self.each_row():
    #         # Generate the row content with walls and cell boundaries
    #         top = "\u2503"  # Left boundary of the row
    #         bottom = "\u2523"  # Left T for the bottom row boundary

    #         for cell in row:
    #             if cell:
    #                 # Two spaces for each cell body
    #                 body = "  "
    #                 top += body

    #                 # Right boundary wall if not linked east
    #                 east_boundary = "\u2503" if not cell.is_linked(cell.east) else " "
    #                 top += east_boundary

    #                 # Bottom wall if not linked south, plus intersection for grid cells
    #                 south_boundary = "\u2501\u2501" if not cell.is_linked(cell.south) else "  "
    #                 intersection = "\u253C" if not cell.is_linked(cell.east) else "\u2523"  # Cross if no links
    #                 bottom += south_boundary + intersection
    #             else:
    #                 # If cell is None, fill with boundary placeholders
    #                 top += "  "  # Empty space for non-existent cells
    #                 bottom += "  "
        
    #         # Complete the right side of the row and add it to output
    #         top += "\u2503\n"  # Right boundary for each row
    #         output += top

    #         # Add the bottom boundary line for each row, adjusting for the last row
    #         if row != self.grid[-1]:  # Skip for the final row to avoid an extra bottom boundary
    #             bottom = bottom + "\u2503\n"  # Right boundary for bottom
    #             output += bottom

    #     # Final bottom border of the maze
    #     output += "\u2517"  # Bottom left corner
    #     for _ in range(self.columns):
    #         output += "\u2501\u2501\u2501"  # Horizontal lines for bottom
    #     output += "\u251B"  # Bottom right corner

    #     return output

    def __str__(self):
    # Top border
        output = "\u250F"  # Top left corner
        for _ in range(self.columns):
            output += "\u2501\u2501\u2501"  # Horizontal lines for top
        output += "\u2513\n"  # Top right corner

        for row in self.each_row():
            # Generate the row content with walls and cell boundaries
            top = "\u2503"  # Left boundary of the row
            bottom = "\u2523"  # Left T for the bottom row boundary

            for cell in row:
                if cell:
                    # Two spaces for each cell body
                    body = "  "
                    top += body

                    # Right boundary wall if not linked east
                    east_boundary = "\u2503" if not cell.is_linked(cell.east) else " "
                    top += east_boundary

                    # Bottom wall if not linked south, plus intersection for grid cells
                    south_boundary = "\u2501\u2501" if not cell.is_linked(cell.south) else "  "
                    bottom += south_boundary + ("\u253B" if not cell.is_linked(cell.east) else "\u2523")
                else:
                    # If cell is None, fill with boundary placeholders
                    top += "  "  # Empty space for non-existent cells
                    bottom += "  "
            
            
            # Complete the right side of the row and add it to output
            top += "\u2503\n"  # Right boundary for each row
            output += top

            # Add the bottom boundary line for each row, adjusting for the last row
            if row != self.grid[-1]:  # Skip for the final row to avoid an extra bottom boundary
                bottom = bottom + "\u2503\n"  # Right T-junction for bottom
                output += bottom

        # Final bottom border of the maze
        output += "\u2517"  # Bottom left corner
        for _ in range(self.columns):
            output += "\u2501\u2501\u2501"  # Horizontal lines for bottom
        output += "\u251B"  # Bottom right corner

        return output

    
    # def __str__(self):
    #     output = "\u250F"  # Top left corner
    #     for col in range(self.columns):
    #         output += "\u2501\u2501"  # Horizontal lines for top
    #     output += "\u2513\n"  # Top right corner

    #     for row in self.each_row():
    #         top = "\u2503"  # Vertical line for left side
    #         for cell in row:
    #             body = "  "  # Two spaces for each cell
    #             top += body
    #         top += "\u2503\n"  # Vertical line for right side
    #         output += top

    #     # Bottom border
    #     output += "\u2517"  # Bottom left corner
    #     for col in range(self.columns):
    #         output += "\u2501\u2501"  # Horizontal lines for bottom
    #     output += "\u251B"  # Bottom right corner
    #     return output

    
    # def __str__(self):
    #     output = "\u250F"  # Top left corner
    #     for _ in range(self.columns):
    #         output += "\u2501\u2501"  # Horizontal lines for top
    #     output += "\u2513\n"  # Top right corner

    #     for row in self.each_row():
    #         top = "\u2503"  # Vertical line for left side
    #         bottom = "\u2523"
    #         for cell in row:
    #             body = "  "  # Two spaces for each cell
    #             top += body
    #         top += "\u2503\n"  # Vertical line for right side
    #         output += top
    #         output = output[:-len(top)]
            

            # for cell in row:
            #     body = " "  # Placeholder space for cell
            #     east_boundary = "" if cell.is_linked(cell.east) else "\u2503"
            #     top += body + east_boundary
                 
                
            #     south_boundary = " " if cell.is_linked(cell.south) else "\u2500"
            #     corner = "\u254B"  # Middle cross for grids
            #     bottom += south_boundary + corner

    #         top = top + "\u257B\n"  # Adding right vertical boundary at end of the top line
    #         output += top
            
    #         # Fix bottom line replacement and corner adjustment
    #         bottom = bottom + "\u252B\n"  # Replace last middle cross with a right "T"
    #         output += bottom

    #     # Correctly handle the final bottom border
    #     output = output[:-len(bottom)]  # Remove the last row's bottom settings
    #     output += "\u2517"  # Bottom left corner
    #     for _ in range(self.columns):
    #         output += "\u2501\u2501"  # Horizontal lines for bottom
    #     output += "\u251B"  # Bottom right corner

    #     return output


   
    # def __str__(self):
    #     output = "\u250C"  # Top left corner using box-drawing character
    #     for col in range(self.columns):
    #         output += "\u2500\u2500"  # Horizontal lines for top
    #     output += "\u2510\n"  # Top right corner

    #     for row in self.each_row():
    #         top = "\u2502"  # Vertical line for left side
    #         bottom ="\u251C"  # Left tee for bottom row

    #         for cell in row:
    #             if not cell:
    #                 cell = Cell(-1, -1)
    #             body = " "
    #             east_boundary = " " if cell.is_linked(cell.east) else "\u2502"
    #             top += body + east_boundary

    #             south_boundary = " " if cell.is_linked(cell.south) else "\u2500"
    #             corner = "\u253C"  # Middle cross for grids
    #             bottom += south_boundary + corner

    #         output += top + "\n"
    #         output += bottom[:-1] + "\u2524\n"

    #     # Replace the bottom line to close the grid
    #     output = output[:-len(bottom) - 1] + "\u2514" + "\u2500" * (len(bottom) - 1) + "\u2518"
    #     return output

