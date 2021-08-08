from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        """
        动态规划
        """
        if prices == None or len(prices) < 2:
            return 0
        length = len(prices)
        hold = - prices[0]
        onHold = 0
        for i in range(1, length):
            onHold = max(onHold, hold + prices[i])
            hold = max(hold, onHold - prices[i])
        return onHold

    def maxProfit2(self, prices: List[int]) -> int:
        """
        贪心算法
        """
        total = 0
        for i in range(0, len(prices)-1):
            total += max(prices[i + 1] - prices[i], 0)
        return total

    def maxProfit3(self, prices: List[int]) -> int:
        """
        贪心算法优化一行python
        """
        return sum([prices[i + 1] - prices[i] for i in range(1, len(prices) - 1) if prices[i + 1] - prices[i] > 0])


if __name__ == '__main__':
    _input = [7, 1, 5, 3, 6, 4]
    A = Solution()
    _output_1 = A.maxProfit1(_input)
    print(_output_1)
    _output_2 = A.maxProfit2(_input)
    print(_output_2)
    _output_3 = A.maxProfit3(_input)
    print(_output_3)














