# Read input
def atmmaintenance(strr: str, strr2: str) -> list[int]:
    """_summary_

    Args:
        strr (str): the number of digits of the output
        strr2 (str): the second numbe, so that we will compare with each amount in the withdraw

    Returns:
        list[int]:the result appended

    problem url:https://open.kattis.com/problems/atmmaintenance
    """
    N, K = map(int, strr.split())
    withdrawals = list(map(int, strr2.split()))

    result = []

    for amount in withdrawals:
        if K >= amount:
            K -= amount
            result.append(1)
        else:
            result.append(0)

    return result
