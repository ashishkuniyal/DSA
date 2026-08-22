class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        sum_digit=0
        product_digit=1
        while n>0:
            digit=n%10
            sum_digit+=digit
            product_digit*=digit
            n//=10
        return original%(sum_digit+product_digit)==0
        