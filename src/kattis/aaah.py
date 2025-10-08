def can_john_go(jon:str,doctor:str) -> str:
    """
    Determines if Jon can go to the doctor based on the number of 'a's in their cries.
    Parameters:
    jon(str)
    doctor(str)
    Returns:
    str:"go" if Jon has enough 'a's, otherwise "no"
    Problem URL:
    https://open.kattis.com/problems/aaah
    """
    jon = jon.strip()
    doctor = doctor.strip()
    return "go" if jon.count('a') >= doctor.count('a') else "no"

print(can_john_go("ahmad","aaa"))