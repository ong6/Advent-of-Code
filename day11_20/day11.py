

def part1():
    f = open("day11.txt", "r")
    data = f.read().split()
    octo_grid = []

    count = [0]

    class octopus:
        def __init__(self, x, y, energy):
            self.x = x
            self.y = y
            self.energy = energy
            self.reset = False

        def increase(self):
            self.energy += 1
            if self.energy == 10:
                self.reset = True
                self.resonate()
                count[0] += 1

        def update(self):
            if self.reset:
                self.energy = 0
                self.reset = False
        
        def resonate(self):
            for x in range(self.x - 1, self.x + 2):
                for y in range(self.y - 1, self.y + 2):
                    if x == self.x and y == self.y:
                        continue
                    if x < 0 or y < 0:
                        continue
                    if x >= len(octo_grid) or y >= len(octo_grid[x]):
                        continue
                    if octo_grid[x][y].energy == 10:
                        continue
                    octo_grid[x][y].increase()
        
        def __repr__(self):
            return "({})".format( self.energy)

    for row in range(len(data)):
        temp_grid = []
        for col in range(len(data[0])):
            temp_grid.append(octopus(row, col, int(data[row][col])))
        octo_grid.append(temp_grid)

    for i in range(100):
        for row in octo_grid:
            for col in row:
                col.increase()
        for row in octo_grid:
            for col in row:
                col.update()

    print(octo_grid)
    print(count)

def part2(steps):
    f = open("day11.txt", "r")
    data = f.read().split()
    octo_grid = []

    count = [0 for i in range(steps)]

    class octopus:
        def __init__(self, x, y, energy):
            self.x = x
            self.y = y
            self.energy = energy
            self.reset = False

        def increase(self, step):
            self.energy += 1
            if self.energy == 10:
                self.reset = True
                self.resonate(step)
                count[step] += 1

        def update(self):
            if self.reset:
                self.energy = 0
                self.reset = False
        
        def resonate(self, step):
            for x in range(self.x - 1, self.x + 2):
                for y in range(self.y - 1, self.y + 2):
                    if x == self.x and y == self.y:
                        continue
                    if x < 0 or y < 0:
                        continue
                    if x >= len(octo_grid) or y >= len(octo_grid[x]):
                        continue
                    if octo_grid[x][y].energy == 10:
                        continue
                    octo_grid[x][y].increase(step)
        
        def __repr__(self):
            return "({})".format( self.energy)

    for row in range(len(data)):
        temp_grid = []
        for col in range(len(data[0])):
            temp_grid.append(octopus(row, col, int(data[row][col])))
        octo_grid.append(temp_grid)

    for i in range(steps):
        for row in octo_grid:
            for col in row:
                col.increase(i)
        for row in octo_grid:
            for col in row:
                col.update()

    print(octo_grid)
    print(count)

    print(count.index(100) + 1)

part2(500)
