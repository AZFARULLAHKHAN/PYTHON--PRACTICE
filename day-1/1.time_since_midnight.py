"""
Question:
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.


Example:
h = 0
m = 1
s = 1

result = 61000  """

# Solution:

def past(h, m, s):
    calculation=((h*3600+m*60+s)*1000)
    print("THE MILLISECONDS SINCE THE MIDNIGHT IS:",calculation)
    return calculation
past(2,12,34)
