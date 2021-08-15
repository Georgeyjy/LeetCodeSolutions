# https://leetcode.com/problems/palindrome-number/submissions/

# def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         return True if str(x) == str(x)[::-1] else False

# def isPalindrome(self, x: int) -> bool:
#     if x < 0:
#         return False
#     x_str = str(x)
#     for i in range(len(x_str) // 2):
#         if x_str[i] != x_str[-(i + 1)]:
#             return False
#     return True


# def isPalindrome(x):
#     if x < 0:
#         return False
#
#     ranger = 1
#     while x / ranger >= 10:
#         ranger *= 10
#
#     while x:
#         left = x // ranger
#         right = x % 10
#         if left != right:
#             return False
#
#         x = (x % ranger) // 10
#         ranger /= 100
#
#     return True

def isPalindrome(x):
    if x < 0 or (x > 0 and x % 10 == 0):
        return False

    result = 0

    while result < x:
        result = result * 10 + x % 10
        x = x // 10

    return True if x == result or x == (result // 10) else False


if __name__ == '__main__':
    isPalindrome(123)
