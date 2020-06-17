"""
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is 
successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is 
successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.
 

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
"""

"""
A basic problem to test the basics to check if you are able to construct your own double edged queue. I am surprised that it has been marked as a medium difficulty problem.
"""

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.ls = [None]*k
        self.b = -1
        self.k = k
         

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        
        if self.b==self.k -1:
            return False
        for i in range(self.b+1,0,-1):
            self.ls[i] = self.ls[i-1]
        self.ls[0]=value
        
        self.b += 1
        
        #print (self.ls,self.b)
        return True
    
    
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.b==self.k-1:
            return False
        else:
            self.b+=1
            self.ls[self.b]=value
            return True
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.ls[0] is None or self.b<0:
            return False
        else:
            for i in range(0,self.b):
                self.ls[i] = self.ls[i+1]
            self.b-=1
            return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.b == -1:
            return False
        else:
            self.ls[self.b] = None
            self.b-=1
            return True
            

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.b==-1:
            return -1
        else:
            return self.ls[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.b==-1:
            return -1
        else:
            return self.ls[self.b]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.b==-1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.b==self.k-1
