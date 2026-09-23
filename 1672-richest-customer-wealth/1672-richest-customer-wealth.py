class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum=0
        for i in range(len(accounts)):
            summ=sum(accounts[i])
            if summ>maximum:
                maximum=summ
        return maximum
        
        