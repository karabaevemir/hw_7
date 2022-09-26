def bubble_sort(num):
    n = len(num)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]

lst = [5, 2, 8, 1, 3, 6, 9, 0, 4]
bubble_sort(lst)

print(f"Bubble sort: {lst}")





a = [1, 4, 3, 2, 5, 8, 6, 7, 9, 0]
a.sort()
print(f'Binary search : {a}')

value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
