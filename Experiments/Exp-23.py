# Exp-23: Alpha-Beta Pruning Algorithm for Gaming

def minimax(depth, node, maximizing_player, values, alpha, beta):

    # Leaf node
    if depth == 3:
        return values[node]

    if maximizing_player:
        best = -float("inf")

        for i in range(2):
            value = minimax(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                print("Branch pruned at depth", depth)
                break

        return best

    else:
        best = float("inf")

        for i in range(2):
            value = minimax(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                print("Branch pruned at depth", depth)
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

alpha = -float("inf")
beta = float("inf")

result = minimax(
    0,
    0,
    True,
    values,
    alpha,
    beta
)

print("\nOptimal value:", result)