def solution(files):
    answer = []
    sorted_file = []
    for file in files:
        name = []
        for i in range(len(file)):
            if file[i].isdigit():
                name.append(file[:i])
                num_tail = file[i:]
                break
        cnt = 0
        for i in range(len(num_tail)):
            if num_tail[i].isdigit() and cnt < 5:
                cnt += 1
            else:
                name.append(num_tail[:i])
                name.append(num_tail[i:])
                break
        else:
            name.append(num_tail)
        sorted_file.append(name)
    sorted_file.sort(key=lambda x:(x[0].lower(), int(x[1])))
    for file in sorted_file:
        answer.append(''.join(file))

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))