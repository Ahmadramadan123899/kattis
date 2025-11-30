from itertools import product


def thought4(queries: list[int]) -> list:
    """_summary_

    Args:
        integ (int): first line, number of the next lines or the number of operations
        queries (list[int]): each one of them should be the answer i of the ith opertation
        if there is no solution that no solution will be displayed
        in each operation we are using : the number 4 , 4 times with: + and/or - and/or / and/or *

    Returns:
        list: For each test case print one line of output containing either an equation using four's to reach the target number or the phrase no solution. Print the equation following the format of the sample output; use spaces to separate the numbers and symbols printed. If there is more than one such equation which evaluates to the target integer, print any one of them.
     problem url:https://open.kattis.com/problems/4thought
    """
    ops = ["+", "-", "*", "/"]
    results = {}
    for op1, op2, op3 in product(ops, repeat=3):
        expr = f"4 {op1} 4 {op2} 4 {op3} 4"
        try:
            val = eval(expr.replace("/", "//"))
            results[val] = expr
        except ZeroDivisionError:
            continue

    output = []
    for q in queries:
        if q in results:
            output.append(f"{results[q]} = {q}")
        else:
            output.append("no solution")

    return output
