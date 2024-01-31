class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)

    def clean(self):
        while True:
            dirty_cells = self.get_dirty_cells()

            if not dirty_cells:
                print("All cells are clean. Mission accomplished!")
                break

            for cell in dirty_cells:
                self.move_to(cell)
                self.clean_cell()

    def get_dirty_cells(self):
        dirty_cells = [(i, j) for i, row in enumerate(self.environment) for j, cell in enumerate(row) if cell == 1]
        return dirty_cells

    def move_to(self, destination):
        print(f"Moving from {self.position} to {destination}")
        self.position = destination

    def clean_cell(self):
        print(f"Cleaning cell {self.position}")
        self.environment[self.position[0]][self.position[1]] = 0

# Example usage:
if __name__ == "__main__":
    # Example environment represented as a 2D grid
    environment = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 1]
    ]

    # Create a VacuumCleaner instance
    vacuum_cleaner = VacuumCleaner(environment)

    # Start cleaning
    vacuum_cleaner.clean()
