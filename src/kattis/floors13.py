def floors(x: int) -> int:
     """_summary_: 
     Bill is responsible for labeling all the floors on a new skyscraper. 
     He's superstitious, so he wants to skip floor 13 while labeling the floors. This means that the 
     12th, 13th,and 14th floors should be labeled 12, 14 and 15  
     respectively. 
        x (int): the number of the floor
          
     Returns:
        int: the corrected one  
     problem url: https://open.kattis.com/problems/13floors
     """
     x = int(x)
     if x >= 13:
      return x + 1
     else:
      return x
     
