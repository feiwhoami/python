"""
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
"""

import queue

class MyQueue:

    def __init__(self):
        self.up = queue.LifoQueue()
        self.down = queue.LifoQueue()


    def push(self, x: int) -> None:
        self.up.put(x)
        return


    # remove the first element
    def pop(self) -> int:
        if not self.down.empty():
            return self.down.get()
        
        while not self.up.empty():
            self.down.put(self.up.get())

        return self.down.get()


    # fetch the first element
    def peek(self) -> int:
        if not self.down.empty():
            return self.down.queue[-1]

        while not self.up.empty():
            self.down.put(self.up.get())

        return self.down.queue[-1]


    def empty(self) -> bool:
        return self.up.empty() and self.down.empty()