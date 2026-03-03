# Queue

q = []

q.append(10)
q.append(20)
print(q)
q.pop(0)
print(q)

# using collections.deque

from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.popleft()
print(queue)