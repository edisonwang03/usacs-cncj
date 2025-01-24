from typing import List


def shortest_path_length(graph: List[List[int]], start: int, end: int) -> int:
    """Find the shortest path length between two nodes in a graph using Dijkstra's algorithm. Assume that such a path does exist.

    Args:
        graph (List[List[int]]): An adjacency matrix representing the graph.
        start (int): The starting node.
        end (int): The ending node.

    Returns:
        int: The shortest path length between the start and end nodes.
    """
    # IMPLEMENT FUNCTION HERE

    # STEP 1: Initialize the distances and visited data structures

    # STEP 2: While the end node is not visited

        # STEP 3: Update the distances to the neighbors of the current node

        # STEP 4: Find the next node with the smallest distance

    # STEP 5: Return the distance to the end node
    return -1


if __name__ == "__main__":
    test_cases = [
        ([[0, 1], [1, 0]], 0, 1, 1),
        ([[0, 1, 4], [1, 0, 2], [4, 2, 0]], 0, 2, 3),
        ([[0, 1, 4, 0], [1, 0, 2, 6], [4, 2, 0, 3], [0, 6, 3, 0]], 0, 3, 6),
    ]

    for graph, start, end, expected in test_cases:
        result = shortest_path_length(graph, start, end)
        print(
            f"shortest_path_length({graph}, {start}, {end}) = {result} (expected: {expected})"
        )
