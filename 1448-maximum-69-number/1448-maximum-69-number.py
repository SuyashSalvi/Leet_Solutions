class Solution:
    def maximum69Number (self, num: int) -> int:
        cur_digit = 0
        index = -1
        num_copy = num

        while num_copy:
            if num_copy % 10 == 6:
                index = cur_digit

            num_copy //= 10
            cur_digit += 1

        return num if index == -1 else num + 3 * 10 ** index