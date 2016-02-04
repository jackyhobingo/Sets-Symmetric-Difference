fist_number=int(input())
first_lists=[int(i) for i in input().split()]
second_number=int(input())
second_lists=[int(i) for i in input().split()]

answer_list=[]
for i in range(0,fist_number):
	if second_lists.count(first_lists[i])==0 and answer_list.count(first_lists[i])==0:
		answer_list.append(first_lists[i])

for i in range(0,second_number):
	if first_lists.count(second_lists[i])==0 and answer_list.count(second_lists[i])==0:
		answer_list.append(second_lists[i])
		
for item in answer_list:
	print (item)