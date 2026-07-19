class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}

        # Store the last occurrence of each character
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):

            # Skip if character already in stack
            if ch in visited:
                continue

            # Remove larger characters if they appear later
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)