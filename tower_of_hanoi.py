def tower_of_hanoi(n, source, auxiliary, destination):

    # Base case
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest disk from source to destination
    print("Move disk", n, "from", source, "to", destination)

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Main program
n = int(input("Enter number of disks: "))

print("\nTower of Hanoi moves:")

tower_of_hanoi(n, 'A', 'B', 'C')

print("\nMinimum number of moves:", 2**n - 1)