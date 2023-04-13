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
            "input": [8, [(10, 10, 3)]],
            "answer": 0,
        },
        {
            "input": [8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]],
            "answer": 12,
        },
        {
            "input": [100, [(1, 1, 100), (2, 1, 50)]],
            "answer": 150,
        },
    ],
    "Extra": [
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
        {
            "input": [50, [(20, 10, 3), (15, 8, 2), (18, 12, 2), (10, 5, 1), (8, 4, 3), (5, 3, 4)]],
            "answer": 99,
        },
    ]
}
