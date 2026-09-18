class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temp=temperatures
        answer = [0] * len(temp)
        stack = []

        for i in range(len(temp)):

            while stack and temp[i] > temp[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)

        return answer
        