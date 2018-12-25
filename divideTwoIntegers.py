class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        temp = int(dividend/divisor)
        return max(-2147483648,min(2147483647,temp))