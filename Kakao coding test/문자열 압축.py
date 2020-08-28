# s = "a"
#
# min_count = 10000000
# for i in range(1, len(s)//2+1):
#     count = 1
#     result = 0
#     for j in range(0, len(s), i):
#         if s[j:j+i] == s[j+i:j+2*i]:
#             count +=1
#         elif j+i > len(s):
#             for k in range(j, len(s)):
#                 result += 1
#         else:
#             if count == 1:
#                 result += i
#             else:
#                 result += i + len(str(count))
#                 count = 1
#
#     if result < min_count:
#         min_count = result
#     if min_count == 10000000:
#         min_count = 2
# print(min_count)

def solution(s):
    answer = len(s)
    for str_len in range(1, len(s)//2+1):
        temp = 0
        start = 0
        end = str_len
        repeat_str = ""
        cnt = 1
        remain = 0
        while end < len(s):
            if len(repeat_str) < str_len:
                repeat_str = s[start:end]
            else:
                if repeat_str == s[end:end+str_len]:
                    cnt += 1
                    start += str_len
                    end += str_len
                else:
                    repeat_str = s[end:end+str_len]
                    if cnt > 1:
                        cnt = 1
                        temp += 1
                    temp += str_len
                    start = end
                    if end + str_len >= len(s):
                        remain = len(s) - end
                    end += str_len
        # print(cnt)
        if cnt > 1:
            temp += (len(str(cnt)) + str_len)
        if remain:
            temp += remain
        # print(temp)
        if temp < answer:
            answer = temp
        # print(answer)

    return answer