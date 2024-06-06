import unittest
from sailing import Sailing

class TestFunctions(unittest.TestCase) :
    """
    Unit test class for testing each method from the Sailing class.
    """

    def test_read_strd_input(self) :
        """
        It tests the 'read_strd_input()' method to ensure it correctly reads input
        from a txt file, and analyses grid dimensions, grid content and queries.
        """
        with open("test_input.txt", "w") as f :
            f.write("9 9 3\n")
            f.write(".........\n")
            f.write(".........\n")
            f.write("....###..\n")
            f.write("...v#....\n")
            f.write("..###....\n")
            f.write("...##...v\n")
            f.write("...##....\n")
            f.write(".........\n")
            f.write("v........\n")
            f.write("1 1\n")
            f.write("9 1\n")
            f.write("5 7\n")
        n, m, q, grid, queries = Sailing.read_strd_input("./test_input.txt")
        self.assertEqual(n, 9)
        self.assertEqual(m, 9)
        self.assertEqual(q, 3)
        self.assertEqual(grid, [".........", ".........", "....###..",
                                "...v#....", "..###....", "...##...v",
                                "...##....", ".........", "v........"])
        self.assertEqual(queries, [(0, 0), (8, 0), (4, 6)])


    def test_dist_to_volcanos(self) :
        """
        It tests the 'dist_to_volcanos()' method to ensure it correctly calculates
        the Manhattan distances from each cell to the nearest volcano 'v'.
        """
        grid = [".........", ".........", "....###..",
                "...v#....", "..###....", "...##...v",
                "...##....", ".........", "v........"]
        manh_dist = Sailing.dist_to_volcanos(9, 9, grid)
        expected_manh_dist = [
            [6, 5, 4, 3, 4, 5, 6, 6, 5],
            [5, 4, 3, 2, 3, 4, 5, 5, 4],
            [4, 3, 2, 1, int(0), int(0), int(0), 4, 3],
            [3, 2, 1, 2, int(0), 5, 4, 3, 2],
            [4, 3, int(0), int(0), int(0), 4, 3, 2, 1],
            [3, 4, 5, int(0), int(0), 3, 2, 1, 2],
            [2, 3, 4, int(0), int(0), 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 5, 4, 3, 2],
            [2, 1, 2, 3, 4, 5, 5, 4, 3]
        ]
        self.assertEqual(manh_dist, expected_manh_dist)


    def test_safe_round_trip(self) :
        """
        It tests the 'safe_round_trip()' method to ensure it correctly calculates
        the maximum safety of a round trip starting from input positions.
        """
        grid = [".........", ".........", "....###..",
                "...v#....", "..###....", "...##...v",
                "...##....", ".........", "v........"]
        manh_dist = [
            [6, 5, 4, 3, 4, 5, 6, 6, 5],
            [5, 4, 3, 2, 3, 4, 5, 5, 4],
            [4, 3, 2, 1, int(0), int(0), int(0), 4, 3],
            [3, 2, 1, 2, int(0), 5, 4, 3, 2],
            [4, 3, int(0), int(0), int(0), 4, 3, 2, 1],
            [3, 4, 5, int(0), int(0), 3, 2, 1, 2],
            [2, 3, 4, int(0), int(0), 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 5, 4, 3, 2],
            [2, 1, 2, 3, 4, 5, 5, 4, 3]
        ]
        self.assertEqual(Sailing.safe_round_trip(0, 0, 9, 9, grid, manh_dist), 3)
        self.assertEqual(Sailing.safe_round_trip(8, 0, 9, 9, grid, manh_dist), 0)
        self.assertEqual(Sailing.safe_round_trip(4, 6, 9, 9, grid, manh_dist), 3)


if __name__ == "__main__" :
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # unittest.main()