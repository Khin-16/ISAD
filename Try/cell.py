# class Cell:
    # def __init__(self, row: int, column: int):
    #     """Initialize the cell with row and column position, and neighbor references."""
    #     self.row = row
    #     self.column = column
    #     self.links = {}  # Dictionary to store linked cells
    #     self.north = None
    #     self.south = None
    #     self.east = None
    #     self.west = None
    #     self.southeast = None


#     def link(self, cell, bidi: bool = True):
#         """Link this cell to another cell, optionally in a bidirectional manner."""
#         self.links[cell] = True
#         if bidi:
#             cell.link(self, False)  # Link back to this cell in the other cell's links
#         return self

    # def unlink(self, cell, bidi: bool = True):
    #     """Unlink this cell from another cell, optionally in a bidirectional manner."""
    #     if cell in self.links:
    #         del self.links[cell]
    #     if bidi:
    #         cell.unlink(self, False)  # Unlink back in the other cell's links
    #     return self

    # def get_links(self):
    #     """Return a list of cells this cell is linked to."""
    #     return list(self.links.keys())

#     def is_linked(self, cell):
#         """Check if this cell is linked to another cell."""
#         return cell in self.links
class Cell:
    def __init__(self, row: int, column: int):
        """Initialize the cell with row and column position, and neighbor references."""
        self.row = row
        self.column = column
        self.links = {}  # Dictionary to store linked cells
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.southeast = None

    def link(self, other, bidi=True):
        """ Link this cell with another cell """
        self.links[other] = True
        if bidi:
            other.link(self, False)

    def is_linked(self, other):
        """ Check if the cell is linked to another cell """
        return other in self.links
    
    def unlink(self, cell, bidi: bool = True):
        """Unlink this cell from another cell, optionally in a bidirectional manner."""
        if cell in self.links:
            del self.links[cell]
        if bidi:
            cell.unlink(self, False)  # Unlink back in the other cell's links
        return self

    def get_links(self):
        """Return a list of cells this cell is linked to."""
        return list(self.links.keys())
    
   