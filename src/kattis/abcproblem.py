def reorder_nb(nums: str, order: str) -> str:
    """_summary_
    Args:
        nums (str): numbers converted to a list expexted : 1 2 3 for ex
        order (str): with respect to this order they will be displayed

    Returns:
        str: the same input nums but displayed in the order "order"
    Problem URL: https://open.kattis.com/problems/abc
    """
    nums = list(map(int, nums.split()))
    order = order.strip()

    nums.sort()
    mapping = {'A': nums[0], 'B': nums[1], 'C': nums[2]}

    return ' '.join(str(mapping[ch]) for ch in order)

nums = "1 2 3"
order = "ACB"
print(reorder_nb(nums, order))