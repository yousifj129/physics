import matplotlib.pyplot as plt
import networkx as nx

def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:  # If the number is even
            n = n // 2
        else:  # If the number is odd
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def build_collatz_tree(n):
    tree = nx.DiGraph()
    for i in range(1, n+1):
        sequence = collatz_sequence(i)
        for j in range(len(sequence) - 1):
            tree.add_edge(sequence[j], sequence[j+1])
    return tree

def draw_collatz_conjecture_tree(n):
    tree = build_collatz_tree(n)
    pos = nx.shell_layout(tree)  # Layout algorithm for tree visualization

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, arrows=True)
    plt.title('Collatz Conjecture Tree for n = {}'.format(n))
    plt.axis('off')
    plt.show()

# Example usage:
draw_collatz_conjecture_tree(100)