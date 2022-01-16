"""
Given n as input, print the following pattern.
Input: n=4
Output:
y1 
y1y2 
y1y2y3 
y1y2y3y4
"""

n = 4
pt = "y"
st = ""
for i in range (1, n+1):
  st = st + pt + str(i)
  print(st)
print("---")

