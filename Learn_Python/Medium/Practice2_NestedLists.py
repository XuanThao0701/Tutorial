a = []

def sort_grade(a):
    for i in range(0, N):
        for j in range(i + 1, N):
            if a[i][1] > a[j][1]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    return a

def runner_up(arr):
    for i in range(0, N):
        if arr[i][1] > arr[0][1]:
            return arr[i][1]

def show_runner_up(arr, ru):
    arr_ru = []
    for i in range(0, N):
        if arr[i][1] == ru:
            arr_ru.append(arr[i])

    print(arr_ru)
    print(len(arr_ru))

N = int(input("N: "))
for i in range(0, N):
    name = input("Name: ")
    grade = float(input("Grade: "))
    a.append([name, grade])

print(a)

sort_grade(a)
print(a)

ru = runner_up(a)

show_runner_up(a, ru)