"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]],
            "answer": 13,
        },
        {
            "input": [8, [(4, 2), (5, 2), (2, 1), (8, 3)]],
            "answer": 21,
        },
        {
            "input": [8, [(10, 10, 3)]],
            "answer": 0,
        },
        {
            "input": [8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]],
            "answer": 12,
        },
    ],
    "C: 0-1": [
        {
            "input": [20, [(5, 9, 1), (4, 10, 1)]],
            "answer": 9,
        },
        {
            "input": [8, [(10, 10, 1)]],
            "answer": 0,
        },
        {
            "input": [15, [(7, 4, 1), (8, 5, 1), (6, 3, 1), (9, 6, 1)]],
            "answer": 24,
        },
        {
            "input": [20, [(10, 5, 1), (15, 8, 1), (7, 4, 1), (12, 6, 1), (4, 2, 1)]],
            "answer": 38,
        },
        {
            "input": [30, [(20, 10, 1), (15, 8, 1), (18, 12, 1), (10, 5, 1), (8, 4, 1), (5, 3, 1)]],
            "answer": 58,
        },
    ],
    "D: Unbounded": [
        {
            "input": [20, [(5, 9), (4, 10)]],
            "answer": 10,
        },
        {
            "input": [8, [(10, 10)]],
            "answer": 0,
        },
        {
            "input": [10, [(4, 3), (2, 2), (6, 4), (3, 1)]],
            "answer": 30,
        },
        {
            "input": [15, [(7, 4), (8, 5), (6, 3), (9, 6)]],
            "answer": 30,
        },
        {
            "input": [20, [(10, 5), (15, 8), (7, 4), (12, 6), (4, 2)]],
            "answer": 40,
        },
        {
            "input": [30, [(20, 10), (15, 8), (18, 12), (10, 5), (8, 4), (5, 3)]],
            "answer": 60,
        },
    ],
    "E: Limited": [
        {
            "input": [100, [(1, 1, 100), (2, 1, 50)]],
            "answer": 150,
        },
        {
            "input": [10, [(4, 3, 2), (2, 2, 1), (6, 4, 3), (3, 1, 1)]],
            "answer": 15,
        },
        {
            "input": [15, [(7, 4, 1), (8, 5, 2), (6, 3, 2), (9, 6, 3)]],
            "answer": 27,
        },
        {
            "input": [40, [(10, 5, 3), (15, 8, 2), (7, 4, 1), (12, 6, 2), (4, 2, 4)]],
            "answer": 78,
        },
    ],
    "F: Extra": [
        {
            "input": [10, [(4, 3), (2, 2, 1), (6, 4, 2), (3, 1)]],
            "answer": 30,
        },
        {
            "input": [9, [(2, 1, 2), (3, 1), (5, 2)]],
            "answer": 27,
        },
        {
            "input": [50, [(20, 10, 1), (15, 8, 2), (18, 12), (10, 5, 1), (8, 4), (5, 3, 4)]],
            "answer": 100,
        },
    ],
}
