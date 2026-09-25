import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:

        # Remove invalid/full indices
        while self.available:
            index = self.available[0]

            if index >= len(self.stacks):
                heapq.heappop(self.available)

            elif len(self.stacks[index]) >= self.capacity:
                heapq.heappop(self.available)

            else:
                break

        if self.available:
            index = heapq.heappop(self.available)
            self.stacks[index].append(val)

            if len(self.stacks[index]) < self.capacity:
                heapq.heappush(self.available, index)

        else:
            self.stacks.append([val])

            index = len(self.stacks) - 1

            if self.capacity > 1:
                heapq.heappush(self.available, index)

    def pop(self) -> int:

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        if not self.stacks:
            return -1

        index = len(self.stacks) - 1
        val = self.stacks[index].pop()

        if self.stacks[index] and len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.available, index)

        return val

    def popAtStack(self, index: int) -> int:

        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()

        heapq.heappush(self.available, index)

        return val