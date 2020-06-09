"""
n passengers board an airplane with exactly n seats. The first passenger has lost the ticket 
and picks a seat randomly. But after that, the rest of passengers will:

Take their own seat if it is still available, 
Pick other seats randomly when they find their seat occupied 
What is the probability that the n-th person can get his own seat?

 Example 1:

Input: n = 1
Output: 1.00000
Explanation: The first person can only get the first seat.
Example 2:

Input: n = 2
Output: 0.50000
Explanation: The second person has a probability of 0.5 to get the second seat (when first 
person gets the first seat).
"""

"""
One of the few mathematical problems in leetcode. The solution will take away all the suspense. 
I used an intuitive approach where every seat in the plane can only be occupied by a passenger 
who arrives before the rightful owner of the seat. But I am copying the mathematical proof here 
from another comment. Runs in O(1) run time with O(1) space.

f(n) = 1/n                               -> 1st person picks his own seat
     + 1/n * 0                           -> 1st person picks last one's seat
	 + (n-2)/n * (                       ->1st person picks one of seat from 2nd to (n-1)th
       1/(n-2) * f(n-1)                  -> 1st person pick 2nd's seat
       1/(n-2) * f(n-2)                  -> 1st person pick 3rd's seat
       ......
       1/(n-2) * f(2)                    -> 1st person pick (n-1)th's seat
	   )
	
=> f(n) = 1/n * ( f(n-1) + f(n-2) + f(n-3) + ... + f(1) )

Now, you can easily get
f(1) = 1
f(2) = 1/2
f(3) = 1/2
...
"""
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n==1:
            return 1
        return 0.5
