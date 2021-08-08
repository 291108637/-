import copy
from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        使用临时数组
        """
        length = len(nums)
        temp = [None for _ in range(length)]
        for i in range(0, length):
            temp[i] = nums[i]
        for j in range(0, length):
            nums[(j + k) % length] = temp[j]
        return nums

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        多次反转一行python
        """
        print(id(nums))
        # nums.append(9)
        b = copy.deepcopy(nums)
        b = 0
        # nums = [1,2,3]
        print(id(nums))
        # nums = nums[::-1][k-1::-1]+nums[::-1][:k-1:-1]
        return b

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        环形旋转
        """
        hold = nums[0]
        index = 0
        length = len(nums)
        visited = [None for _ in range(length)]
        for i in range(0, length):
            index = (index + k) % length
            if (visited[index]):
                index = (index + 1) % length
                hold = nums[index]
                i -= 1
            else:
                visited[index] = True
                temp = nums[index]
                nums[index] = hold
                hold = temp
        return nums

if __name__ == '__main__':
    _input, k = [1, 2, 3, 4, 5, 6, 7], 3
    print(_input)
    A = Solution()
    # _output_1 = A.rotate1(_input, k)
    # print(_output_1)
    # _input, k = [1, 2, 3, 4, 5, 6, 7], 3
    _output_2 = A.rotate2(_input, k)
    # print(_output_2)
    print(_input)
    print(id(_input))
    # _output_3 = A.rotate3(_input, k)
    # print(_output_3)
    # print('--------------')
    # a = [1,2,3,4,5]
    # print(id(a),a)
    # a[0:3]
    # print(id(a),a)




