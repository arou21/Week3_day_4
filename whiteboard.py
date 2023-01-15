# Consecutive Indices
# You are given a list of unique integers (arr), and two integers (a and b). Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).
# Example:
# Input: ([3,1,0,19,4], 19, 5)	
# Output: False
# Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)				
# Output: True
# Input: ([3,1,0,19], 19, 0)	
# Output: True
		
def consectively(nums,a,b):
    x = None
    y =None
    if a not in nums or b not in nums:
        return False
    for i in range(len(nums)):
        if nums[i] == a:
            x=i
        elif nums[i] == b:
            y = i

    if x -y == 1 or x-y ==-1:
        return True
    return False
consectively ([1, 6, 9, -3, 4, -78, 0], -3, 4)

#code wars
# find the shortest

def find_short(s):
    x =s.split()
    ans= len(x[0])
    for y in x:
        if len(y) < ans:
            ans = len(y)
        return ans


