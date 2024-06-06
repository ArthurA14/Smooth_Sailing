from collections import deque
import os
from memory_profiler import profile # To test the performance of the algorithm

class Sailing :
    """
    'Sailing' class for the maximum safety distance calculation algorithm.
    """

    @staticmethod
    @profile
    def read_strd_input(filename="./input.txt") :
        """
        This method reads data from an input file. The file should include grid dimensions (n, m),
        the number of queries 'q', the grid representation (with '.', 'v', and '#'),
        and the queries (each specifying a start position).
        """
        if not os.path.isfile(filename) :
            raise FileNotFoundError(f"This file {filename} doesn't exist yet.")

        with open(filename, 'r') as f :
            input = f.readline().split()
            n, m, q = int(input[0]), int(input[1]), int(input[2])
            grid = [f.readline().strip() for _ in range(n)]
            # 'queries' contains (x, y) coordinates
            queries = [(int(line.strip().split()[0]) - 1, int(line.strip().split()[1]) - 1) for line in f.readlines()]

        return n, m, q, grid, queries


    @staticmethod
    @profile
    def dist_to_volcanos(n, m, grid) :
        """
        This method calculates the Manhattan distances from each cell to the nearest underwater volcano 'v',
        using the Breadth-First Search (BFS) algorithm to cross the grid and then to compute these required distances.
        """
        manh_dist = [m*[int(0)] for _ in range(n)]
        tail = deque() # to pop elements from the left of the collection.

        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 'v' :
                    manh_dist[i][j] = 0
                    tail.append((i, j))

        # print(tail)
        orientations = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while tail :
            x, y = tail.popleft()

            for (dx, dy) in orientations :
                rx, ry = x+dx, y+dy
                if 0 <= rx < n and 0 <= ry < m and manh_dist[rx][ry] == int(0) :
                    if grid[rx][ry] == '.' or grid[rx][ry] == 'v' :
                        manh_dist[rx][ry] = manh_dist[x][y] + 1
                        tail.append((rx, ry))

        # print(manh_dist)
        return manh_dist


    @staticmethod
    @profile
    def safe_round_trip(x, y, n, m, grid, manh_dist) :
        """
        This method determines the maximum safety of a round trip starting from (x, y) coordinates,
        using BFS to explore the grid and to calculate the maximum safety distance to any volcano encountered during the trip.
        """
        tail = deque([(x, y)])
        covered_ground = set()
        covered_ground.add((x, y))
        maximum_safety = manh_dist[x][y]

        orientations = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while tail :
            qx, qy = tail.popleft()
            movements_list = list()
            for (dx, dy) in orientations :
                rx, ry = qx+dx, qy+dy
                if 0 <= rx < n and 0 <= ry < m and (rx, ry) not in covered_ground :
                    if grid[rx][ry] == 'v' or grid[rx][ry] == '.' :
                        tail.append((rx, ry))
                        covered_ground.add((rx, ry))
                movements_list.append((rx, ry))

            for (rx, ry) in movements_list :
                if 0 <= rx < n and 0 <= ry < m :
                    if grid[rx][ry] == '.' or grid[rx][ry] == 'v':
                        if manh_dist[rx][ry] > maximum_safety :
                            pass
            
            maximum_safety = min(manh_dist[rx][ry]
                                 for (rx, ry) in movements_list
                                 if 0 <= rx < n and 0 <= ry < m)
        
        return maximum_safety


@profile
def launch() :
    """
    This method launches the entire algorithm above.
    """
    n, m, q, grid, queries = Sailing.read_strd_input()
    manh_dist = Sailing.dist_to_volcanos(n, m, grid)

    outputs = list()
    for (x, y) in queries :
        maximum_safety = Sailing.safe_round_trip(x, y, n, m, grid, manh_dist)
        outputs.append(maximum_safety)

    for output in outputs :
        print(output)


if __name__ == "__main__" :
    launch()