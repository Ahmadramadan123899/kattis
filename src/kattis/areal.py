import math
def areal(strr: str) -> float:
    """_summary_ computing the perimetre of an input

    Args:
        strr (str): input number 

    Returns:
        float: per output which 4*the square of the input
    problem url: https://open.kattis.com/problems/areal
    """
    a = int(strr)
    side = math.sqrt(a)
    perimeter = 4 * side
    return f"{perimeter:.6f}"

print(areal("5"))
