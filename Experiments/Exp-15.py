# Exp-15: Vacuum Cleaner Problem

# State:
# (location, left_room, right_room)
# 0 = Dirty
# 1 = Clean

def vacuum_cleaner():
    state = ["A", 0, 0]

    print("Initial State:", state)

    # Clean room A
    if state[0] == "A" and state[1] == 0:
        print("Suck dirt from Room A")
        state[1] = 1

    # Move to room B
    print("Move from Room A to Room B")
    state[0] = "B"

    # Clean room B
    if state[0] == "B" and state[2] == 0:
        print("Suck dirt from Room B")
        state[2] = 1

    print("\nFinal State:", state)


vacuum_cleaner()