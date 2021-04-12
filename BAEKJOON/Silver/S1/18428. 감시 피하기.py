def teacher_see(teacher):
    

N = int(input())
data = [list(input().split()) for i in range(N)]
student = []
teacher = []
arr = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if data[i][j] == 'S' :
            student.append([i,j])
            arr[i][j] = 'S'
        elif data[i][j] == 'T' :
            teacher.append([i,j])
            arr[i][j] = 'T'
