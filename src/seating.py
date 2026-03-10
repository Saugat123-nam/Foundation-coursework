"""
Task 2 — P vs NP: Seating Arrangement Problem
Demonstrates brute force (exhaustive) vs heuristic approaches.
"""

from itertools import permutations


STUDENTS = ["Asha", "Bikash", "Nisha", "Rohan", "Suman"]

FRIENDS = {
    ("Asha", "Bikash"),
    ("Nisha", "Rohan"),
    ("Bikash", "Suman"),
}

SAME_CITY = {
    ("Asha", "Nisha"),
    ("Rohan", "Suman"),
}


def is_valid(arrangement: list) -> bool:
    """Check no adjacent pair are friends or from the same city."""
    for i in range(len(arrangement) - 1):
        a, b = arrangement[i], arrangement[i + 1]
        pair = (min(a, b), max(a, b))
        friends_norm = {(min(x, y), max(x, y)) for x, y in FRIENDS}
        city_norm    = {(min(x, y), max(x, y)) for x, y in SAME_CITY}
        if pair in friends_norm or pair in city_norm:
            return False
    return True


def brute_force(students: list) -> list | None:
    """Exhaustively check every permutation — O(n!)."""
    for perm in permutations(students):
        if is_valid(list(perm)):
            return list(perm)
    return None


def heuristic(students: list, friends: set, same_city: set) -> list | None:
    """
    Greedy heuristic: place the most-constrained student first.
    Reduces search space without guaranteeing optimality.
    """
    def constraint_count(s):
        return sum(1 for a, b in friends | same_city if s in (a, b))

    remaining = sorted(students, key=constraint_count, reverse=True)
    arrangement = []

    for student in remaining:
        placed = False
        for pos in range(len(arrangement) + 1):
            candidate = arrangement[:pos] + [student] + arrangement[pos:]
            if is_valid(candidate):
                arrangement = candidate
                placed = True
                break
        if not placed:
            return None

    return arrangement


def run_demo():
    print("\n" + "=" * 50)
    print("TASK 2 — P vs NP: SEATING ARRANGEMENT")
    print("=" * 50)
    print(f"Students : {STUDENTS}")
    print(f"Friends  : {FRIENDS}")
    print(f"Same City: {SAME_CITY}\n")

    result_bf = brute_force(STUDENTS)
    print(f"Brute Force Result  : {result_bf}")

    result_h = heuristic(STUDENTS, FRIENDS, SAME_CITY)
    print(f"Heuristic Result    : {result_h}")

    print(f"\nTotal permutations checked (worst case): {len(STUDENTS)}! = "
          f"{__import__('math').factorial(len(STUDENTS))}")
