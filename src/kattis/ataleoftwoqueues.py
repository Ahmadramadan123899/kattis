import sys
def atableoftwoqueues(lines: list[str]) -> str:
    """_summary_

    Args:
        lines (list[str]): first line the user should enter the number of people in the queue at the left the at the right
                           Second line, we have to enter the time in second for each person waiting in the queue at the left
                         third line, we have to enter the time in second for each person waiting in the queue at the right
    Returns:               
        str: If it is quicker for Unnar to enter the left queue, output “left”.
        If it is quicker for Unnar to enter the right queue, output “right”.
        If it does not matter which queue Unnar enters, output “either”.
    
    problem url: https://open.kattis.com/problems/ataleoftwoqueues
    """
    n,m=map(int,lines[0].strip().split())
    left=list(map(int,lines[1].strip().split()))
    right=list(map(int,lines[2].strip().split()))

    left_time=sum(left)
    right_time=sum(right)

    if left_time<right_time:
        return "left"
    elif right_time<left_time:
        return "right"
    else:
        return "either"

input_lines= sys.stdin.readlines()
str22=atableoftwoqueues(input_lines)
print(str22)