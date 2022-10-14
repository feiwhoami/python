"""
Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively.
You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
"""

from queue import Queue

class MyStack:

    def __init__(self):
        self.up = Queue()
        self.down = Queue()


    def push(self, x: int) -> None:
        self.up.put(x)
        return


    # remove the last element
    def pop(self) -> int:
        if self.up.empty():
            while not self.down.empty():
                self.up.put(self.down.get())

        while self.up.qsize() > 1:
            self.down.put(self.up.get())

        return self.up.get()


    # fetch the last element
    def top(self) -> int:
        if self.up.empty():
            while not self.down.empty():
                self.up.put(self.down.get())

        while self.up.qsize() > 1:
            self.down.put(self.up.get())

        return self.up.queue[0]


    def empty(self) -> bool:
        return self.up.empty() and self.down.empty()
