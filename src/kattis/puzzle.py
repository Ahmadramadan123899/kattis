from collections import deque

def solve_puzzle(lines: list[str]) -> int:
    """_summary_

    Args:
        lines (list[str]): The input will consist of exactly 2 lines, each containing exactly 
                        2 characters.
                        Each character is either a number 1 through 3 (representing one of the tiles) or a dash (-) (the empty space).
                        The puzzle state represented by the input is guaranteed to be a solvable configuration.

    Returns: Output a singe integer, indicating the minimum number of moves required to solve the puzzle from the provided starting position, or 
             0 if it's already in the solved position.
        int: _description_
    """
    goal = "123-"
    start = ''.join(line.strip() for line in lines[:2])

    #Directions: up, down, left, right
    moves = {
        0: [1, 2],      #top-left
        1: [0, 3],      #top-right
        2: [0, 3],      #bottom-left
        3: [1, 2]       #bottom-right
    }

    queue = deque([(start, 0)])
    visited = set()

    while queue:
        state, depth = queue.popleft()
        if state == goal:
            return depth
        if state in visited:
            continue
        visited.add(state)

        idx = state.index('-')
        for swap in moves[idx]:
            lst = list(state)
            lst[idx], lst[swap] = lst[swap], lst[idx]
            new_state = ''.join(lst)
            queue.append((new_state, depth + 1))

    return -1  

input_data = ["2-", "13"]
print(solve_puzzle(input_data))
