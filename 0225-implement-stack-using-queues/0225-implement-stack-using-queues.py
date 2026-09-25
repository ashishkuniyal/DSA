from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def move_front_to_back(self):
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        self.move_front_to_back()
        return self.q.popleft()

    def top(self) -> int:
        self.move_front_to_back()

        x = self.q.popleft()
        self.q.append(x)

        return x

    def empty(self) -> bool:
        return len(self.q) == 0