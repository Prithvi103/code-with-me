"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the 
definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 
0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 
0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong 
to the range of [-100, 100]. And the output should be also in this form.
"""

"""
I fail to understand how this can be a medium level difficulty problem if it can be coded in 11 
lines. This is a straightforward multiplication problem with O(1) run time and space consumption
"""

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        if a is None or b is None:
            return "0+0i"
        w1,x1 = a.split('+')
        y1,z1 = b.split('+')
        w=int(w1)
        y= int(y1)
        x=int(x1[:len(x1)-1])
        z=int(z1[:len(z1)-1])
        return str(w*y-x*z)+'+'+str(w*z + x*y)+'i'