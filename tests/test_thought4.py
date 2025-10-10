from src.kattis.thought4 import thought4

def eval_expression(expr: str) -> int:
    """Helper to evaluate the expression string returned by thought4."""
    return eval(expr.split('=')[0].replace('/', '//'))

def test_known_solutions():
    queries = [0, 7, 24, 9]
    results = thought4(queries)
    for query, result in zip(queries, results):
        assert eval_expression(result) == query

def test_no_solution():
    queries = [100, -10]
    expected = ["no solution", "no solution"]
    assert thought4(queries) == expected