fist_number = int(input())
set1 = set(map(int, input().split(" ")))
second_number = int(input())
set2 = set(map(int, input().split(" ")))

symmetric_difference  = set1.symmetric_difference(set2)

for i in sorted(list(symmetric_difference)):
    print(i)
