def different(lines: list[str]) -> list[int]:
    """_summary_

    Args:
        lines (list[str]): list of the intered numbers from the command line

    Returns:
        list[int]:the absolute difference for each line
    problem url: https://open.kattis.com/problems/different

    """
    results = []
    for line in lines:
        a, b = map(int, line.strip().split())
        results.append(abs(a - b))
    return results
