# Queue

A queue is an ordered collection of items where the addition of new items happens at one end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.”
This ordering principle is called FIFO, first-in first-out.
The stack operations are given below.

- Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
- enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
- dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
- is_empty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
- size() returns the number of items in the queue. It needs no parameters and returns an integer.

### Implementing a Queue in Python 

- queue.py

### Hot Potato Game

In this game children line up in a circle and pass an item from neighbor to neighbor as fast as they can. 
At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. 
Play continues until only one child is left.

- hot_potato.py


