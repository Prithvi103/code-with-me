"""
You are given a doubly linked list which in addition to the next and previous pointers, it 
could have a child pointer, which may or may not point to a separate doubly linked list. These 
child lists may have one or more children of their own, and so on, to produce a multilevel data 
structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are 
given the head of the first level of the list.

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The output would be:
1---2---3---7---8---11---12---9---10---4---5---6---NULL
"""

"""
Took me some time to solve. I was quick to identify that we had to recurse and keep track of 
where the ending node in the child path had to rejoin in the parent path but I hit some 
infinite recursion on the way to solving this problem. Solution runs in O(n) time as it visits 
each node once.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        tmp = head
        self.traverse(tmp,tmp.next,None)
        return head
        
    def traverse(self, cur:'Node',nxt:'Node', jmp:'Node'):
        child = cur.child
        if cur is None:
            return
        if child is not None:
            cur.next = child
            cur.child = None
            child.prev = cur
            self.traverse(child, child.next, nxt)
        if cur.next is None:
            if jmp is not None:
                cur.next = jmp
                jmp.prev = cur
            return
        cur = nxt
        if cur is None:
            return
        self.traverse(cur,cur.next,jmp)
        return
        
