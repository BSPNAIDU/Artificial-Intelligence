# Exp-13: Crypt-Arithmetic Problem
# SEND + MORE = MONEY

from itertools import permutations

letters = "SENDMORY"

for values in permutations(range(10), len(letters)):
    mapping = dict(zip(letters, values))

    # Leading letters cannot be zero
    if mapping["S"] == 0 or mapping["M"] == 0:
        continue

    SEND = (
        mapping["S"] * 1000 +
        mapping["E"] * 100 +
        mapping["N"] * 10 +
        mapping["D"]
    )

    MORE = (
        mapping["M"] * 1000 +
        mapping["O"] * 100 +
        mapping["R"] * 10 +
        mapping["E"]
    )

    MONEY = (
        mapping["M"] * 10000 +
        mapping["O"] * 1000 +
        mapping["N"] * 100 +
        mapping["E"] * 10 +
        mapping["Y"]
    )

    if SEND + MORE == MONEY:
        print("Solution found:")
        print(mapping)
        print()
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        break