class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk=[]
        for ops in operations:
            if ops =="+":
                stk.append(stk[-1]+stk[-2])
            elif ops=="D":
                stk.append(stk[-1]*2)
            elif ops=="C":
                stk.pop()
            else:
                stk.append(int(ops))
        return sum(stk)
        