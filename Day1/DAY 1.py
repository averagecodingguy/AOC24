x = open('/workspaces/AOC24/Day1/Input.txt', 'r')
Lines = x.readlines()
x.close()
Left_List, Right_List = [], []
for i in range (1000):
    temp = Lines[i].split('   ')
    Left_List.append(int(temp[0]))
    Right_List.append(int(temp[1].strip()))
Left_List.sort()
Right_List.sort()
sum = 0
for i in range(1000):
    sum += max(Right_List[i], Left_List[i]) - min(Right_List[i], Left_List[i])
print(sum)

sum = 0
for i in Left_List:
    count = Right_List.count(i)
    sum += count*i
print(sum)