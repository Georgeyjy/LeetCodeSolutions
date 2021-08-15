# https://leetcode.com/problems/reverse-integer/submissions/

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        res_str = ""
        try:
            int(x[0])
        except:
            sign = x[0]
            x = x[1:]
            res_str = sign + x[::-1]
        if not res_str:
            res_str = x[::-1]
        res = int(res_str)
        if -(2 ** 31) <= res <= 2 ** 31 - 1:
            return res
        else:
            return 0

class Solution:
    def reverse(self, x: int) -> int:
        ret = int(str(x).strip("-")[::-1])
        ret = ret if x > 0 else -ret
        return ret if ret >= -2 ** 31 and ret <= 2 ** 31 -1 else 0