# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# def lengthOfLongestSubstring(s: str) -> int:
#     if len(s) == 0:
#         return 0
#     if len(s) == 1:
#         return 1
#     tmp, res = 1, 0
#
#     for i in range(len(s)):
#         for j in range(i + 1, len(s)):
#             if s[j] not in s[i:j]:
#                 tmp += 1
#             else:
#                 break
#         if tmp > res:
#             res = tmp
#         tmp = 1
#
#     return res


def lengthOfLongestSubstring(s: str) -> int:
    last_idx = {}
    max_len = 0

    start_idx = 0

    for i in range(0, len(s)):

        if s[i] in last_idx:
            start_idx = max(start_idx, last_idx[s[i]] + 1)

        max_len = max(max_len, i - start_idx + 1)

        last_idx[s[i]] = i

    return max_len


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))
