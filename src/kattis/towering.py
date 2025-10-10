from itertools import combinations
def towering(data:list[int]) -> list[int]:
    """_summary_

    Args:
        integers (list[int]):list of integers entered , its about 
        The input consists of eight positive integers. The first six represent the heights of the six boxes. These values will be given in no particular order and no two will be equal.
        The last two values (which will never be the same) are the heights of the two towers.
        All box heights will be < or equal to 100 and the sum of the box heights will equal the sum of the tower heights.
    
    Returns:
        list[int]:Output the heights of the three boxes in the first tower (i.e., the tower specified by the first tower height in the input), then the heights of the three boxes in the second tower. Each set of boxes should be output in order of decreasing height. Each test case will have a unique answer.
    problem url: https://open.kattis.com/problems/towering
    """
    boxes=data[:6]
    tower1,tower2=data[6],data[7]
    for combo in combinations(boxes,3):
        group1=list(combo)
        group2=[x for x in boxes if x not in group1]
        if sum(group1)==tower1 and sum(group2)==tower2:
            finallist= sorted(group1,reverse=True)+sorted(group2,reverse=True)
            return finallist
        elif sum(group1)==tower2 and sum(group2)==tower1:
            finallist= sorted(group2,reverse=True)+sorted(group1,reverse=True)
            return finallist