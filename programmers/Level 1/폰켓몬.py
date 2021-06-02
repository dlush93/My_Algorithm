def solution(nums):
    answer = 0
    select = len(nums)//2
    monster = list(set(nums))
    if len(monster) > select:
        answer = select
    else:
        answer = len(monster)
    return answer